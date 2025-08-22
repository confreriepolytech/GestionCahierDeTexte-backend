import os

from inspect import signature

import jwt
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.utils.encoding import DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from rest_framework import serializers, status
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken


from GestionCahierDeTexte import settings
from accounts import google
from accounts.models import Professeur, SecretaireGeneral, SecretaireClasse, Classe, CustomUser
from accounts.register import register_social_user
from accounts.utils import Util

User = get_user_model() # accounts.CustomerUser





class UserRegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    nom = serializers.CharField()
    prenom = serializers.CharField()
    role = serializers.ChoiceField(choices=[
        ('secretaire_general', 'Secretaire General'),
        ('professeur', 'Professeur'),
        ('secretaire_classe', 'Secretaire Classe'),
    ])

    # specific fields
    departement = serializers.ChoiceField(required=False,
                                          choices=[('Génie_Civil','Génie Civil'),
                                            ('Génie_Electrique','Génie Electrique'),
                                            ('Génie_Mécanique','Génie Mécanique'),
                                            ('Génie_Informatique','Génie Informatique')],
                                          help_text='Required only for Secretaire general',
                                          allow_blank=True,
                                          allow_null=False)
    """id_classe = serializers.SlugRelatedField(
        queryset=Classe.objects.all(),
        required=False,
        allow_null=True,
        help_text="Required only for secretaire_classe",
        write_only=True,
        slug_field="nom_licence",
    )"""
    classe = serializers.ChoiceField(choices=[c.nom_licence for c in Classe.objects.all()],
                                        required=False,
                                        allow_null=False,
                                        help_text="Required only for secretaire_classe",
                                        write_only=True,)
    signature = serializers.ImageField(
        required=False,
        write_only=True,
        allow_null=True,
        help_text="Required only for professeur",
    )



    def validate(self, data):
        role = data.get('role')
        nom = data.get('nom')
        prenom =  data.get('prenom')
        email = data.get('email')


        required_fields = {
            'secretaire_general': ['departement'],
            'secretaire_class': ['id_classe'],
        }

        #check for missing fields
        missing = [field for field in required_fields.get(role, [])
                  if not data.get(field)]

        if missing:
            raise serializers.ValidationError({
                field: f"This field is required for {role}"
                for field in missing
            })

        # check if the user exist already or his email is already taken by someone else
        if CustomUser.objects.filter(nom=nom , prenom=prenom).exists() or CustomUser.objects.filter(email=email) :
            raise serializers.ValidationError({'Please Login to your accounts or contact admin'})

        return  data

    def create(self, validated_data):
        role = validated_data.get("role")
        email=  validated_data.get("email")
        nom = validated_data.get("nom")
        prenom = validated_data.get("prenom")
        password = validated_data.get("password")
        departement = validated_data.get("departement")
        classe = validated_data.get("classe")
        signature = validated_data.get("signature")


        # get the classe
        id_classe = get_object_or_404(Classe , nom_licence=classe)
        #create user
        user = User.objects.create_user(email=email,
                                   role=role,
                                   nom=nom,
                                   prenom=prenom,
                                   password=password,
                                   last_login=timezone.now())


        # Create role-specific instance
        if role == 'secretaire_general':

            SecretaireGeneral.objects.create(user_id=user,
                                             departement=departement)

        elif role == 'professeur':

            Professeur.objects.create(user_id=user,
                                      signature=signature)


        elif role == 'secretaire_classe':
            SecretaireClasse.objects.create(user_id=user,
                                            id_classe=id_classe)

        else:
            raise serializers.ValidationError("Invalid role")

        return user
















class PasswordTokenCheckSerializer(serializers.Serializer):
    uidb64 = serializers.CharField()
    token = serializers.CharField()


    def validate(self, attrs):
        uidb64 = attrs['uidb64']
        token = attrs['token']

        try:
            id = urlsafe_base64_decode(uidb64).decode()  # decoding uidb64 and convert it to  int object
            user = User.objects.get(id=id)

            # check if token belongs to the user
            if not PasswordResetTokenGenerator().check_token(user, token):
                 raise ValidationError({"error detail": "Token is not valid , request to new one!"})

            return attrs #see later

        except (User.DoesNotExist, DjangoUnicodeDecodeError):
            raise ValidationError({"error detail ": "Token is not valid , request to new one !"})


class VerifyEmailSerializer(serializers.Serializer):

    """ Given a token and validate it , if the token is not valid or expired , raise an error"""

    token = serializers.CharField()

    def validate_token(self, token):

        try:
            payload = jwt.decode(token,settings.SECRET_KEY, algorithms=["HS256"])
            user = User.objects.get(id=payload['user_id'])

            if not user.is_verified:
                self.context['user'] = user

            return token

        except jwt.ExpiredSignatureError:
            raise ValidationError({"error": "Token expired !"})

        except jwt.exceptions.DecodeError:
            raise ValidationError({"error": "Token is invalid"})




class GoogleSocialAuthSerializer(serializers.Serializer):
    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        user_data = google.Google.validate(auth_token)
        try:
            user_data['sub']

        except KeyError:
            raise serializers.ValidationError('the token is invalid or expired . Please login again')

        if user_data['aud'] != os.environ.get('GOOGLE_CLIENT_ID'):

            raise AuthenticationFailed('oops , who are you ?')

        user_id = user_data['sub']
        email = user_data['email']
        name = user_data['name']
        provider = 'Google'


        return register_social_user(
            provider=provider,
            user_id=user_id,
            email=email,
            name=name,
        )


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(min_length=10)
    password = serializers.CharField(min_length=5, write_only=True)
    tokens = serializers.CharField(read_only=True)
    #username = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'tokens',]


    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        filtered_user_by_email = User.objects.filter(email=email)



        user = authenticate(email=email, password=password)


        """if filtered_user_by_email.exists() and filtered_user_by_email[0].auth_provider!= 'email' :
            print(filtered_user_by_email[0].auth_provider, 'hello')
            #raise AuthenticationFailed("please continue your login using " + filtered_user_by_email[0].auth_provider)"""

        if not user:
            raise AuthenticationFailed('Invalid credentials , try again.')
        if not user.is_active:
            raise AuthenticationFailed('Account is disabled. contact admin')
        if not  user.is_verified:
            raise AuthenticationFailed('Email is not verified')

        user.last_login = timezone.now()
        user.save(update_fields=['last_login'])

        return {
            'email': user.email,
            'password': password,
            #'username': user.username,
            'tokens':user.tokens()
        }


class LogoutSerializer(serializers.Serializer):

    refresh = serializers.CharField()


    def validate(self, attrs):
        refresh_token = attrs.get('refresh')

        try:
            RefreshToken(refresh_token)
        except TokenError:
            raise ValidationError({'refresh': 'Token is invalid or expired'})

        return attrs

    def save(self, **kwargs):
        refresh_token = self.validated_data['refresh']

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
        except TokenError:
            raise ValidationError({'refresh': 'Token could not be blacklisted'})



class ResetPasswordEmailRequestSerializer(serializers.Serializer):

    email = serializers.EmailField(write_only=True)


    def validate_email(self, value):


        try :
            user = User.objects.get(email=value)
        except User.DoesNotExist:
            #raise ValidationError('email is not exist')
            raise ValidationError({"error": "Email does not exist"})

        self.context['user'] = user

        return value


class SetNewPasswordSerializer(serializers.Serializer):

    password = serializers.CharField(min_length=5, write_only=True)
    token = serializers.CharField(write_only=True)
    uidb64 = serializers.CharField(write_only=True)


    class Meta:
        fields = ['password', 'token', 'uidb64']


    def validate(self, attrs):
        try:
            password = attrs.get('password')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')

            id = int(urlsafe_base64_decode(uidb64).decode())

            user = User.objects.get(id=id)

            #token verification
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed('the reset link is invalid', 401)

            attrs['user'] = user

            return attrs


        except  (User.DoesNotExist, ValueError, TypeError):
            raise AuthenticationFailed('the reset link is invalid', 401)









#--------------------------------------------------------------------------------------------------------












class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['user_id', 'nom', 'prenom','role', 'email']  # Champs communs aux users

class SecretaireGeneralSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = SecretaireGeneral
        fields = BaseUserSerializer.Meta.fields + ['departement']

class SecretaireClasseSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = SecretaireClasse
        fields = BaseUserSerializer.Meta.fields # + ['champ_specifique_user2']

class ProfesseurSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = Professeur
        ields = BaseUserSerializer.Meta.fields + ['signature']
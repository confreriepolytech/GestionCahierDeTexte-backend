
from jsonschema.exceptions import ValidationError
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

from accounts.models import Professeur, SecretaireClasse, SecretaireGeneral
from accounts.permissions import IsSecretaireGeneral


import re
from base64 import urlsafe_b64encode, urlsafe_b64decode
from logging import raiseExceptions

import jwt
from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.db import connection
from django.urls import reverse
from django.utils.encoding import smart_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from accounts.serializers import UserRegistrationSerializer, ResetPasswordEmailRequestSerializer, \
    SetNewPasswordSerializer, LoginSerializer, LogoutSerializer, GoogleSocialAuthSerializer, \
    PasswordTokenCheckSerializer, VerifyEmailSerializer, ProfesseurSerializer
from django.contrib.auth import login, authenticate, get_user_model
from rest_framework import status, views, generics
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.utils import Util


User = get_user_model()


class UserRegistrationView(APIView):
    serializer_class = UserRegistrationSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]  # Add file upload support(for signature)

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user= serializer.save() #serializer.save() call create method of my serializer ,and this method return user

        token = RefreshToken.for_user(user).access_token

        current_site = get_current_site(request).domain
        relative_link = reverse('user-email-verify')
        absurl = 'http://' + current_site + relative_link + '?token=' + str(token) #absolute url to our website
        email_body = "Hi " + user.nom +  " " + user.prenom + " please use the link bellow to verify your email \n" + absurl
        data = {'email_body':email_body, 'to_email':user.email,
                'email_subject':'verify your email', }
        Util.send_mail(data)


        # Build response data
        response_data = {
            'message': 'successful registration ! ',
            'user_id': user.id,
            'email': user.email,
            'role': user.role
        }


        # Add role-specific information( ID , .....)  in the response  data
        if user.role == 'professeur':
            response_data['has_signature'] = user.professeur.has_signature #Add signature status for professeur
            # here maybe I should make a try catch to verify if role-specific user exist
            response_data['professeur_id'] = user.professeur.id
        elif user.role == 'secretaire_general':
            response_data['secretaire_general_id'] = user.secretairegeneral.id
        elif user.role == 'secretaire_classe':
            response_data['secretaire_classe_id'] = user.secretaireclasse.id
        else:
            # if role is invalid
            #  I  think I  have already verified this condition in the serializer
            return Response({"message":"Invalid role "}, status=status.HTTP_400_BAD_REQUEST)


        # it is possible to make "user.professeur" or "user.secretaire_general" because django creates a reverse relation ( one to one field ) in customuser model

        return Response(response_data, status=status.HTTP_201_CREATED)





class GoogleSocialAuthView(generics.GenericAPIView):

    serializer_class =  GoogleSocialAuthSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = (serializer.validated_data['auth_token'])
        return Response(data, status=status.HTTP_200_OK)


class VerifyEmailView(generics.GenericAPIView):

    serializer_class = VerifyEmailSerializer

    def get(self, request):
        token = request.GET.get('token')

        serializer = self.serializer_class(data={"token":token})
        serializer.is_valid(raise_exception=True)

        user = serializer.context.get('user')
        if  user and not user.is_verified:
            user.is_verified = True
            user.save()

        return Response({"email successfully verified !"}, status=status.HTTP_200_OK)




class LoginView(views.APIView):


    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)






class LogoutView(generics.GenericAPIView):
    """ logout view , required user is authenticated """

    #permission_classes = (IsAuthenticated,)
    serializer_class = LogoutSerializer


    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)



class RequestPasswordReset(generics.GenericAPIView):

    """If user requests a password reset, we will email him with a reset link."""


    serializer_class = ResetPasswordEmailRequestSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)


        user = serializer.context.get('user')

        # Generate reset token
        # uidb64 = urlsafe_b64encode(user.id)
        uidb64 = urlsafe_base64_encode(str(user.id).encode())
        token = PasswordResetTokenGenerator().make_token(user)

        # Create reset link
        current_site = get_current_site(request=self.context.get('request')).domain
        relative_link = reverse('password-reset-confirm',
                                kwargs={'uidb64': uidb64, 'token': token})
        absurl = 'http://' + current_site + relative_link  # http will be change in https later

        # Send email
        email_body = f"Hi {user.username} use this link below to reset your password /n {absurl}"
        email_information = {'email_body': email_body, 'to_email': user.email, 'email_subject': 'reset your password'}
        Util.send_mail(email_information)

        return Response({"message": "We have sent you a password reset email"},
                            status=status.HTTP_200_OK)


class PasswordTokenCheckAPIView(generics.GenericAPIView):
    """ check if the password token  belongs to the user and
     is  valid  """

    serializer_class = PasswordTokenCheckSerializer

    def get(self, request, uidb64, token):
        serializer = self.serializer_class(data={'uidb64': uidb64, 'token': token})
        serializer.is_valid(raise_exception=True)

        return Response({'success': True,
                         'message': 'credentials are valid',
                         'uidb64': uidb64,
                         'token': token},status=status.HTTP_200_OK)




class SetNewPasswordAPIView(generics.GenericAPIView):

    """Allow user to set a new password"""

    serializer_class = SetNewPasswordSerializer


    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        password = serializer.validated_data['password']

        user.set_password(password)
        user.save()

        return Response({"success": True, "message": "Password updated successfully"},
                        status=status.HTTP_200_OK)






class UploadSignatureAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, prof_id):
        try:
            professeur = Professeur.objects.get(pk=prof_id)
        except Professeur.DoesNotExist:
            return Response({"error": "Professeur non trouvé"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProfesseurSerializer(professeur, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Signature téléversée avec succès", "data": serializer.data},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
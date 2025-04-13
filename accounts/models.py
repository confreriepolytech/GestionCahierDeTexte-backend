from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import  PermissionsMixin
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):

        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    AUTH_PROVIDERS = {'google': 'google', 'email': 'email', 'apple': 'apple'}

    ROLE_CHOICES = [('professeur', 'professeur'),
                    ('secretaire_general', 'sécrétaire général'),
                    ('secretaire_classe', 'sécrétaire de classe'),
                    ('admin', 'admin')]


    email = models.EmailField(unique=True, db_index=True)
    nom = models.CharField(max_length=150, blank=True)
    prenom = models.CharField(max_length=150, blank=True)
    role = models.CharField(max_length=23, choices=ROLE_CHOICES, blank=True, db_index=True)
    auth_provider = models.CharField(max_length=10, default=AUTH_PROVIDERS.get('email'))
    is_active = models.BooleanField(default=True, db_index=True)
    is_staff = models.BooleanField(default=False, db_index=True)
    is_verified = models.BooleanField(default=False, db_index=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password"]


    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }


    class Meta:
        pass
        #managed = False
        db_table = 'utilisateur'






class SecretaireGeneral(models.Model):
    user = models.OneToOneField("accounts.CustomUser", on_delete=models.CASCADE, db_index=True)
    departement = models.CharField(max_length=100)

    class Meta:
        #managed = False
        db_table = 'secretairegeneral'



class Professeur(models.Model):
    user = models.OneToOneField("accounts.CustomUser", on_delete=models.CASCADE, db_index=True)
    signature = models.ImageField(upload_to='signatures/', blank=True, null=True)

    @property
    def has_signature(self):
        return bool(self.signature)


    class Meta:
        #managed = False
        db_table = 'professeur'


class SecretaireClasse(models.Model):
    user = models.OneToOneField("accounts.CustomUser", on_delete=models.CASCADE, db_index=True)
    id_classe = models.ForeignKey("CahierDeTexte.classe", models.DO_NOTHING, db_column='id_classe', blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'secretaireclasse'


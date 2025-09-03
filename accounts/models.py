

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import  PermissionsMixin
from django.db import models
from django.utils import timezone
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
        extra_fields.setdefault('is_verified', True)
        extra_fields.setdefault('role', 'admin')
        extra_fields.setdefault('date_joined', timezone.now())
        extra_fields.setdefault('last_login', timezone.now())
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('nom','superadmin')
        extra_fields.setdefault('prenom', 'superadmin')

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    AUTH_PROVIDERS = {'google': 'google', 'email': 'email', 'apple': 'apple'}

    ROLE_CHOICES = [('professeur', 'professeur'),
                    ('secretaire_general', 'sécrétaire général'),
                    ('secretaire_classe', 'sécrétaire de classe'),
                    ('admin', 'admin')]


    email = models.EmailField(unique=True, db_index=True)
    nom = models.CharField(max_length=150, blank=False, null=False)
    prenom = models.CharField(max_length=150, blank=False, null=False)
    role = models.CharField(max_length=23, choices=ROLE_CHOICES, blank=False, null=False, db_index=True)
    date_joined = models.DateTimeField(default=timezone.now)


    auth_provider = models.CharField(max_length=10, default=AUTH_PROVIDERS.get('email'))
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False, db_index=True)
    is_verified = models.BooleanField(default=False, db_index=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password"]



    def tokens(self):
        refresh = RefreshToken.for_user(self)

        return {
            'refresh_token': str(refresh),
            'access_token': str(refresh.access_token),
        }


    class Meta:
        ordering = ['role']
        db_table = 'utilisateur'


    def __str__(self):
       return f"{self.nom} {self.prenom}"



class SecretaireGeneral(models.Model):
    user_id = models.OneToOneField("accounts.CustomUser", on_delete=models.CASCADE, db_index=True)
    departement = models.CharField(choices=[('GC','Génie Civil'),
                                            ('GE','Génie Electrique'),
                                            ('GM','Génie Mécanique'),
                                            ('GI','Génie Informatique')],
                                   max_length=100, blank=False, null=False)

    class Meta:
        #managed = False
        db_table = 'secretairegeneral'



class Professeur(models.Model):
    user_id = models.OneToOneField("accounts.CustomUser", on_delete=models.CASCADE, db_index=True)
    signature = models.ImageField(upload_to='signatures/', blank=True, null=True)

    @property
    def has_signature(self):
        return bool(self.signature)


    class Meta:
        # managed = False
        verbose_name = 'professeur'
        verbose_name_plural = 'professeurs'
        ordering = ["-user_id"]
        db_table = 'professeur'


    def __str__(self):
        return f"{self.user_id.nom} {self.user_id.prenom}"





class Classe(models.Model):
    id_classe = models.AutoField(primary_key=True)
    nom_licence = models.CharField(max_length=100, blank=False, null=False)
    niveau = models.CharField(max_length=50, blank=False, null=False)
    departement = models.CharField(choices = [('GC','Génie Civil'),
                                            ('GE','Génie Electrique'),
                                            ('GM','Génie Mécanique'),
                                            ('GI','Génie Informatique'),
                                            ('TC','Tronc Commun')],
                                        max_length=100, blank=False, null=False)
    mention = models.CharField(max_length=23,
                               choices=[('LF', 'Licence Fondamentale'),
                                        ('LP', 'Licence Professionelle')],
                               blank=False, null=False)
    class Meta:
        #managed = False
        verbose_name = 'classe'
        verbose_name_plural = 'classes'
        ordering=['-mention']
        db_table = 'classe'

    def __str__(self):
        return self.nom_licence



class SecretaireClasse(models.Model):
    user_id = models.OneToOneField("accounts.CustomUser", on_delete=models.CASCADE, db_index=True)
    #id_classe = models.ForeignKey("accounts.Classe", on_delete=models.SET_NULL, db_column='id_classe', blank=True, null=True)
    id_classe = models.ForeignKey("accounts.Classe", on_delete=models.SET_NULL, db_column='id_classe', blank=True,
                                  null=True)
    class Meta:
        #managed = False
        db_table = 'secretaireclasse'






#-------------------------------------cahier de texte-----------------------------------














class Seance(models.Model):
    id_seance = models.AutoField(primary_key=True)
    id_professeur = models.ForeignKey("accounts.Professeur", on_delete=models.CASCADE, db_column='id_professeur', blank=True, null=True)
    #id_ues = models.ForeignKey('CahierDeTexte.Ue', on_delete=models.CASCADE, db_column='id_UEs', blank=True, null=True)  # Field name made lowercase.
    sous_session_seance = models.CharField(max_length=1000,blank=False, null=False)
    id_classe = models.ForeignKey("accounts.Classe", on_delete=models.CASCADE, db_column='id_classe', blank=True, null=True)
    id_ues = models.ForeignKey("accounts.Ue", on_delete=models.CASCADE, db_column='id_UEs')
    date_heure = models.DateTimeField(null=False, blank=False, db_index=True)

    class Meta:
        #managed = False
        db_table = 'seance'

class Cahiertexte(models.Model):
    id_cahier = models.AutoField(primary_key=True)
    id_classe = models.ForeignKey("accounts.Classe", on_delete=models.CASCADE, db_column='id_classe')
    id_secretaire = models.ForeignKey("accounts.SecretaireClasse", on_delete=models.CASCADE, db_column='id_secretaire')

    date_de_creation = models.DateTimeField(auto_now_add=True)# la date de creation
    date_de_mise_a_jour = models.DateTimeField(auto_now=True)# date de mise a jour

    class Meta:
        db_table = 'cahiertexte'
        #managed = False
        verbose_name = 'Cahiertexte'
        verbose_name_plural = 'Cahiertextes'
        ordering = ['-date_de_creation']

    def __str__(self):
        return f"Cahier {self.id_cahier} - Classe {self.id_classe}"

class Validation(models.Model):

    STATUS_CHOICES = [('valide', 'validé'),
                      ('non_valide', 'non validé')]
    id_validation = models.AutoField(primary_key=True)
    id_cahier = models.ForeignKey(Cahiertexte, on_delete=models.CASCADE, db_column='id_cahier')
    id_professeur = models.ForeignKey("accounts.Professeur", on_delete=models.CASCADE, db_column='id_professeur',)
    #id_ues = models.ForeignKey("CahierDeTexte.Ue", on_delete=models.CASCADE, db_column='id_UEs')  # Field name made lowercase.
    id_ues = models.ForeignKey("accounts.Ue", on_delete=models.CASCADE, db_column='id_UEs')
    statut = models.CharField(max_length=11 , choices=STATUS_CHOICES, blank=False, null=False, db_index=True)
    id_seance = models.ForeignKey(Seance, on_delete=models.CASCADE, db_column='id_seance',)
    date_validation = models.DateTimeField(null=False, blank=False)
    #signature = models.ImageField(upload_to='validations/',blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'validation'







#ues models



class Ue(models.Model):
    id_UEs = models.AutoField(primary_key=True)
    code_UEs = models.CharField(max_length=50, unique=True, db_index=True)
    intitule_UEs = models.CharField(max_length=255)
    id_prof = models.ForeignKey("accounts.Professeur", on_delete=models.SET_NULL, db_column='id_prof', null=True)  # Assure la correspondance avec la colonne SQL

    crenaux =  models.JSONField(default=dict)
    #classe = models.ForeignKey("CahierDeTexte.Classe", on_delete=models.SET_NULL,null=True)
    classe = models.ForeignKey("accounts.Classe", on_delete=models.SET_NULL, null=True)



    class Meta:
        # managed = False

        verbose_name = 'ue'
        verbose_name_plural = 'ues'
        ordering = ['-classe']
        db_table = 'ues'  # Correspond au nom exact de la table dans MySQL

    def __str__(self):
        return f"{self.code_UEs} - {self.intitule_UEs}- {self.classe}"


class Fichier_Ue(models.Model):
    id_Fichiers_Ue = models.AutoField(primary_key=True)
    #id_UEs = models.ForeignKey("CahierDeTexte.Ue", on_delete=models.CASCADE, db_column='id_UEs')
    id_UEs = models.ForeignKey("accounts.Ue", on_delete=models.CASCADE, db_column='id_UEs')
    lien_fichier = models.FileField(upload_to='fichiers_ue/')

    class Meta:
        #managed = False

        ordering = ['-id_UEs']
        db_table = 'fichiers_ue'

    def __str__(self):
        return self.lien_fichier



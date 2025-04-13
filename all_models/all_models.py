# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cahiertexte(models.Model):
    id_cahier = models.AutoField(primary_key=True)
    id_classe = models.ForeignKey('Classe', models.DO_NOTHING, db_column='id_classe', blank=True, null=True)
    id_secretaire = models.ForeignKey('Secretaireclasse', models.DO_NOTHING, db_column='id_secretaire', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cahiertexte'


class Classe(models.Model):
    id_classe = models.AutoField(primary_key=True)
    nom_licence = models.CharField(max_length=100)
    niveau = models.CharField(max_length=50)
    departement = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'classe'


class Professeur(models.Model):
    id_prof = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.CharField(unique=True, max_length=100)
    mot_de_passe = models.CharField(max_length=255)
    signature = models.ImageField(upload_to='signatures/', blank=True, null=True)  # Chemin de stockage des signatures

    class Meta:
        managed = False
        db_table = 'professeur'


class Seance(models.Model):
    id_seance = models.AutoField(primary_key=True)
    id_professeur = models.ForeignKey(Professeur, models.DO_NOTHING, db_column='id_professeur', blank=True, null=True)
    id_ues = models.ForeignKey('Ues', models.DO_NOTHING, db_column='id_UEs', blank=True, null=True)  # Field name made lowercase.
    id_classe = models.ForeignKey(Classe, models.DO_NOTHING, db_column='id_classe', blank=True, null=True)
    date_heure = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'seance'


class Secretaireclasse(models.Model):
    id_secc = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.CharField(unique=True, max_length=100)
    mot_de_passe = models.CharField(max_length=255)
    id_classe = models.ForeignKey(Classe, models.DO_NOTHING, db_column='id_classe', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'secretaireclasse'


class Secretairegeneral(models.Model):
    id_sec = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.CharField(unique=True, max_length=100)
    mot_de_passe = models.CharField(max_length=255)
    departement = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'secretairegeneral'


class Ues(models.Model):
    id_ues = models.AutoField(db_column='id_UEs', primary_key=True)  # Field name made lowercase.
    code_ues = models.CharField(db_column='code_UEs', unique=True, max_length=50)  # Field name made lowercase.
    intitule_ues = models.CharField(db_column='intitule_UEs', max_length=255)  # Field name made lowercase.
    id_prof = models.ForeignKey(Professeur, models.DO_NOTHING, db_column='id_prof', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ues'


class Validation(models.Model):
    id_validation = models.AutoField(primary_key=True)
    id_cahier = models.ForeignKey(Cahiertexte, models.DO_NOTHING, db_column='id_cahier', blank=True, null=True)
    id_professeur = models.ForeignKey(Professeur, models.DO_NOTHING, db_column='id_professeur', blank=True, null=True)
    id_ues = models.ForeignKey(Ues, models.DO_NOTHING, db_column='id_UEs', blank=True, null=True)  # Field name made lowercase.
    statut = models.CharField(max_length=11)
    id_seance = models.ForeignKey(Seance, models.DO_NOTHING, db_column='id_seance', blank=True, null=True)
    date_validation = models.DateTimeField()
    signature = models.ImageField(upload_to='validations/',blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'validation'

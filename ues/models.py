from django.db import models

from accounts.models import Professeur


class Ue(models.Model):
    id_UEs = models.AutoField(primary_key=True)
    code_UEs = models.CharField(max_length=50, unique=True)
    intitule_UEs = models.CharField(max_length=255)
    id_prof = models.ForeignKey("accounts.Professeur", on_delete=models.CASCADE,
                                db_column='id_prof')  # Assure la correspondance avec la colonne SQL

    class Meta:
        # managed = False
        db_table = 'UEs'  # Correspond au nom exact de la table dans MySQL

    def __str__(self):
        return f"{self.code_UEs} - {self.intitule_UEs}"


class Fichier_Ue(models.Model):
    id_Fichiers_Ue = models.AutoField(primary_key=True)
    id_UEs = models.ForeignKey("ues.Ue", on_delete=models.CASCADE, db_column='id_UEs')
    lien_fichier = models.FileField(upload_to='fichiers_ue/')

    class Meta:
        #managed = False
        db_table = 'Fichiers_Ue'

    def __str__(self):
        return self.lien_fichier



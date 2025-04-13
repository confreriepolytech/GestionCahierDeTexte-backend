from django.db import models



from ues.models import Professeur,Ue





class Classe(models.Model):
    id_classe = models.AutoField(primary_key=True)
    nom_licence = models.CharField(max_length=100)
    niveau = models.CharField(max_length=50)
    departement = models.CharField(max_length=100)

    class Meta:
        #managed = False
        db_table = 'classe'


class Seance(models.Model):
    id_seance = models.AutoField(primary_key=True)
    id_professeur = models.ForeignKey(Professeur, models.DO_NOTHING, db_column='id_professeur', blank=True, null=True)
    id_ues = models.ForeignKey('ues.Ue', models.DO_NOTHING, db_column='id_UEs', blank=True, null=True)  # Field name made lowercase.
    id_classe = models.ForeignKey(Classe, models.DO_NOTHING, db_column='id_classe', blank=True, null=True)
    date_heure = models.DateTimeField()

    class Meta:
        #managed = False
        db_table = 'seance'

class Cahiertexte(models.Model):
    id_cahier = models.AutoField(primary_key=True)
    id_classe = models.ForeignKey(Classe, on_delete=models.CASCADE, db_column='id_classe')
    id_secretaire = models.ForeignKey("accounts.SecretaireClasse", on_delete=models.CASCADE, db_column='id_secretaire')

    date_de_creation = models.DateTimeField(auto_now_add=True)# la date de creation
    date_de_mise_a_jour = models.DateTimeField(auto_now_add=True)# date de mise a jour

    class Meta:
        db_table = 'Cahiertexte'
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
    id_cahier = models.ForeignKey(Cahiertexte, models.DO_NOTHING, db_column='id_cahier', blank=True, null=True)
    id_professeur = models.ForeignKey(Professeur, models.DO_NOTHING, db_column='id_professeur', blank=True, null=True)
    id_ues = models.ForeignKey(Ue, models.DO_NOTHING, db_column='id_UEs', blank=True, null=True)  # Field name made lowercase.
    statut = models.CharField(max_length=11 , choices=STATUS_CHOICES)
    id_seance = models.ForeignKey(Seance, models.DO_NOTHING, db_column='id_seance', blank=True, null=True)
    date_validation = models.DateTimeField()
    signature = models.ImageField(upload_to='validations/',blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'validation'










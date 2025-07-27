from django.contrib import admin


from accounts.models import Professeur, SecretaireClasse, SecretaireGeneral, CustomUser, Classe, Fichier_Ue, Validation, \
    Seance, Ue, Cahiertexte

admin.site.register(CustomUser)
admin.site.register(Professeur)
admin.site.register(SecretaireClasse)
admin.site.register(SecretaireGeneral)

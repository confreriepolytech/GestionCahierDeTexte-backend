from django.contrib import admin

from accounts.models import Classe, Cahiertexte, Ue, Fichier_Ue, Validation, Seance

admin.site.register(Classe)
admin.site.register(Cahiertexte)
admin.site.register(Ue)
admin.site.register(Fichier_Ue)
admin.site.register(Validation)
admin.site.register(Seance)

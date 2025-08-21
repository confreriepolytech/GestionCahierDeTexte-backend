from django.contrib import admin

from accounts.models import Classe, Cahiertexte, Ue, Fichier_Ue, Validation, Seance

@admin.register(Classe)
class ClasseAdmin(admin.ModelAdmin):
    readonly_fields = (id,)


@admin.register(Cahiertexte)
class CahiertexteAdmin(admin.ModelAdmin):
    readonly_fields = (id,)

@admin.register(Ue)
class UeAdmin(admin.ModelAdmin):
    readonly_fields = (id,)

admin.site.register(Fichier_Ue)
admin.site.register(Validation)
admin.site.register(Seance)

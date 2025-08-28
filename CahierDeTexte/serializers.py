from django.shortcuts import get_object_or_404
from jsonschema.exceptions import ValidationError
from rest_framework import serializers # Carlos tu te rappelle de ce dont je te parlait la derniere fois la c'est sa qui se repete ici de mme que dans ton serializer de accounts

from accounts.models import Seance, Cahiertexte, SecretaireClasse, Fichier_Ue, Ue, Classe, Validation


#from .models import Cahiertexte, Seance
#from accounts.models import SecretaireClasse, Classe
#from .models import Ue, Fichier_Ue







class SeanceCreateSerializer(serializers.ModelSerializer):

  def validate(self, attrs):
      cahier_id = attrs.get('cahier_id')
      cahier = get_object_or_404(Cahiertexte, id=cahier_id)

      # Vérification des doublons pour la classe, date, et UE
      date = attrs.get("date")
      id_ue = attrs.get("id_ue")

      if Seance.objects.filter(id_classe=cahier.id_classe, id_ue=id_ue, date_heure=date).exists():
          raise ValidationError("Une séance pour cette classe, UE, et date existe déjà.")

  def create(self, validated_data):
      cahier_id = validated_data.get("cahier_id")
      date = validated_data.get("date")
      sous_session_seance = validated_data.get("contenu ")
      id_professeur = validated_data.get("professeur")
      id_ue = validated_data.get("id_ue"),
      id_classe = cahier_id.id_classe.id

      seance = Seance.objects.create(cahier=cahier_id,
                            date=date,
                            sous_session_seance=sous_session_seance,
                            id_professeur=id_professeur,
                            id_ue=id_ue,
                            id_classe=id_classe)

      Validation.objects.create(
          id_cahier=cahier_id,
          id_professeur=seance.id_professeur,
          id_ues=seance.id_ue,
          id_seance=seance,
          statut="non validé"
      )
  class Meta:
    model = Seance
    fields = '__all__'

  # Serializer pour le Cahier de Texte

class SeanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seance
        fields = '__all__'

class CahiertexteSerializer(serializers.ModelSerializer):
  id_classe = serializers.PrimaryKeyRelatedField(queryset=Classe.objects.all())  # Gérer la relation avec Classe
  id_secretaire = serializers.PrimaryKeyRelatedField(queryset=SecretaireClasse.objects.all())
  seances = SeanceSerializer(many=True, read_only=True)  # Afficher les séances liées au cahier

  class Meta:
    model = Cahiertexte
    fields = '__all__'


def validate(self, data):
  # Logique pour vérifier si un cahier existe déjà pour la classe et le secrétaire
  id_classe = data.get('id_classe')
  id_secretaire = data.get('id_secretaire')

  if Cahiertexte.objects.filter(id_classe=id_classe, id_secretaire=id_secretaire).exists():
    raise serializers.ValidationError("Un cahier de texte pour cette classe et ce secrétaire existe déjà.")

  return data




#ues serializer



class UeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ue
        fields = '__all__'


class ClasseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classe
        fields = '__all__'


class FichierUeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fichier_Ue
        fields = '__all__'




class HTMLUploadSerializer(serializers.Serializer):
    file = serializers.FileField(required=True)

    def validate_file(self, value):
        # Vérifier que le fichier a bien une extension .html
        if not value.name.endswith('.html'):
            raise serializers.ValidationError("Le fichier doit être au format HTML.")
        return value









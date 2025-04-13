
from rest_framework import serializers # Carlos tu te rappelle de ce dont je te parlait la derniere fois la c'est sa qui se repete ici de mme que dans ton serializer de accounts
from .models import Cahiertexte, Seance, Classe
from accounts.models import SecretaireClasse


class SeanceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Seance
    fields = '__all__'

  # Serializer pour le Cahier de Texte


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

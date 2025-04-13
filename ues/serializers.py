from rest_framework import serializers
from .models import Ue, Fichier_Ue

class UeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ue
        fields = '__all__'


class FichierUeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fichier_Ue
        fields = '__all__'


class HTMLUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

    def validate_file(self, value):
        # Vérifier que le fichier a bien une extension .html
        if not value.name.endswith('.html'):
            raise serializers.ValidationError("Le fichier doit être au format HTML.")
        return value




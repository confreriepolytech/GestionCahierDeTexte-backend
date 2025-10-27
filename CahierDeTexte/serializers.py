from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from pyasn1.type.useful import UTCTime

from rest_framework import serializers # Carlos tu te rappelle de ce dont je te parlait la derniere fois la c'est sa qui se repete ici de mme que dans ton serializer de accounts
from rest_framework.exceptions import ValidationError

from accounts.models import Seance, Cahiertexte, SecretaireClasse, Fichier_Ue, Ue, Classe, Validation, Professeur


#from .models import Cahiertexte, Seance
#from accounts.models import SecretaireClasse, Classe
#from .models import Ue, Fichier_Ue

User = get_user_model()




class SeanceDetailsSerialiser(serializers.Serializer):
    nom_classe = serializers.ChoiceField(choices=[classe.nom_licence for classe in Classe.objects.all()],
                                         help_text='give the name of a valid classe ',
                                         )
    mention = serializers.ChoiceField(choices=[('LF', 'Licence Fondamentale'),
                                        ('LP', 'Licence Professionelle')])
    """departement = serializers.ChoiceField(
                                          choices=[('GC', 'Génie Civil'),
                                                   ('GE', 'Génie Electrique'),
                                                   ('GM', 'Génie Mécanique'),
                                                   ('GI', 'Génie Informatique')],

                                          )"""


    code_ue = serializers.ChoiceField(choices=[ue.code_UEs for ue in Ue.objects.all()],
                                      help_text='give a valid ue code',
                                      )



    def validate(self, attrs):
        nom_classe = attrs.get('nom_classe')
        code_ue = attrs.get('code_ue')

        mention = attrs.get('mention')

        classe = get_object_or_404(Classe , nom_licence=nom_classe,  mention=mention)
        print(type(classe))
        ue = get_object_or_404(Ue , code_UEs=code_ue, classe=classe)

        attrs["classe"] = classe
        attrs["ue"] = ue
        return attrs


class SeanceCreateSerializer(serializers.ModelSerializer):
  code_UEs = serializers.ChoiceField(choices=[ue.code_UEs for ue in Ue.objects.all()],
                                     required=True, write_only=True )

  nom_classe = serializers.ChoiceField(choices=[classe.nom_licence for classe in Classe.objects.all()],
                                       help_text='give the name of a valid classe ',
                                       write_only=True )

  mention = serializers.ChoiceField(choices=[('LF', 'Licence Fondamentale'),
                                             ('LP', 'Licence Professionelle')],
                                    write_only=True)

  professeur_email = serializers.ChoiceField(choices=[prof.user_id.email for prof in Professeur.objects.all()],
                                             write_only=True )

  def validate(self, attrs):
      #cahier_id = attrs.get('cahier_id')
      #cahier_de_texte = get_object_or_404(Cahiertexte, id=cahier_id)
      professeur_email = attrs.get('professeur_email')

      nom_classe = attrs.get('nom_classe')
      code_UEs = attrs.get('code_UEs')
      mention = attrs.get('mention')

      user_professeur = get_object_or_404(User, email=professeur_email)
      professeur = user_professeur.professeur
      print(type(professeur))
      attrs["professeur"] = professeur
      classe = get_object_or_404(Classe, nom_licence=nom_classe, mention=mention)
      cahier_de_texte = get_object_or_404(Cahiertexte, id_classe=classe)
      attrs["cahier_de_texte"] = cahier_de_texte

      # Vérification des doublons pour la classe, date, et UE
      date = attrs.get("date")
      ue = get_object_or_404(Ue, code_UEs=code_UEs, classe=classe)
      id_classe = classe
      attrs["id_classe"] = id_classe
      id_ue = ue
      attrs["id_ue"]= id_ue
      print(id_ue, "hello1")

      if Seance.objects.filter(id_classe=cahier_de_texte.id_classe, id_ues=id_ue, date_heure=date).exists():
          raise ValidationError("Une séance pour cette classe, UE, et date existe déjà.", 400)

      return attrs

  def create(self, validated_data):
      cahier_de_texte_id = validated_data.get("cahier_de_texte")
      date = validated_data.get("date_heure")
      sous_session_seance = validated_data.get("sous_session_seance")
      id_professeur = validated_data.get("professeur")
      print(id_professeur, "hello2")
      id_ue = validated_data.get("id_ue")
      print(id_ue, "hello3")
      id_classe = validated_data.get("id_classe")
      print(id_classe, "hello4")
      seance = Seance.objects.create(
                                     date_heure=date,
                                     sous_session_seance=sous_session_seance,
                                     id_professeur=id_professeur,
                                     id_ues=id_ue,
                                     id_classe=id_classe)

      validation = Validation.objects.create(
          id_cahier=cahier_de_texte_id,
          id_professeur=seance.id_professeur,
          id_ues=seance.id_ues,
          id_seance=seance,
          statut="non validé"
      )
      validated_data["validation_id"] = validation.id_validation
      return seance

  class Meta:
    model = Seance
    #fields = ["sous_session_seance","date_heure"]
    #read_only_fields = ["id_classe", "id_professeur", "id_ues"]
    fields = '__all__'
    read_only_fields = ["id_classe", "id_professeur", "id_ues"]

  # Serializer pour le Cahier de Texte

class SeanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seance
        fields = '__all__'

class CahiertexteSerializer(serializers.ModelSerializer):
  id_classe = serializers.PrimaryKeyRelatedField(queryset=Classe.objects.all())  # Gérer la relation avec Classe
  id_secretaire = serializers.PrimaryKeyRelatedField(queryset=SecretaireClasse.objects.all())
  seances = SeanceSerializer(many=True, read_only=True)  # Afficher les séances liées au cahier

  def validate(self, data):
      # Logique pour vérifier si un cahier existe déjà pour la classe et le secrétaire
      id_classe = data.get('id_classe')
      id_secretaire = data.get('id_secretaire')

      if Cahiertexte.objects.filter(id_classe=id_classe, id_secretaire=id_secretaire).exists():
          raise serializers.ValidationError("Un cahier de texte pour cette classe et ce secrétaire existe déjà.")

      return data

  class Meta:
    model = Cahiertexte
    fields = '__all__'






#ues serializer



class UeSerializer(serializers.ModelSerializer):

    """def validate(self, attrs):
        code_UEs = attrs.get('code_UEs')
        intitule_UEs = attrs.get('intitule_UEs')
        id_prof = attrs.get('id_prof')
        classe = attrs.get('classe')

        if Ue.objects.filter(code_UEs=code_UEs,intitule_UEs=intitule_UEs,id_classe=classe, d_prof=id_prof).exists():
            raise ValidationError("cette Ue existe déjà")

        return attrs"""

    class Meta:
        model = Ue
        fields = '__all__'


class ClasseSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        nom_licence = attrs.get('nom_licence')
        niveau = attrs.get('niveau')
        departement = attrs.get('departement')
        mention = attrs.get('mention')

        if Classe.objects.filter(nom_licence=nom_licence, niveau=niveau, departement=departement, mention=mention).exists():
            raise ValidationError("cette classe existe déjà", 400)

        return attrs
    class Meta:
        model = Classe
        fields = '__all__'



class ClasseScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classe
        fields = ['id_classe', 'nom_licence', 'niveau', 'schedule']
        #fields = ['id_classe', 'nom_licence', 'niveau']


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










import os
from django.utils import timezone
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import generics, permissions, status
from django.http import FileResponse
from django.conf import settings

from weasyprint import HTML
from rest_framework.parsers import MultiPartParser, FormParser


from accounts.permissions import IsSecretaireClasse, IsProfesseur, IsCustomAdmin
#from ues.serializers import UeSerializer
#from GestionCahierDeTexte import settings
from .serializers import CahiertexteSerializer, SeanceSerializer, FichierUeSerializer, HTMLUploadSerializer, \
    UeSerializer, ClasseSerializer, SeanceCreateSerializer, SeanceDetailsSerialiser, ClasseScheduleSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
#from .models import Cahiertexte, Validation, Seance, Fichier_Ue, Ue
#from ues.models import  Ue
from accounts.models import Professeur, Classe, Cahiertexte, Ue, Seance, Validation, Fichier_Ue

"""
class IsSecretary(permissions.BasePermission):
    

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.groups.filter(name='secretaire').exists()"""


#good
class CahiertexteCreateView(generics.CreateAPIView):
    """
    Vue pour créer un cahier de texte.
    Accessible uniquement aux secrétaires.
    """
    queryset = Cahiertexte.objects.all()
    serializer_class = CahiertexteSerializer
    #permission_classes = [permissions.IsAuthenticated, IsSecretaireClasse]

    @extend_schema(tags=["Cahier-de-texte"])
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CahiertexteListView(generics.ListAPIView):

    """
    Vue pour lister les cahiers de texte.
    Accessible à tous les utilisateurs authentifiés.
    """
    queryset = Cahiertexte.objects.all()
    serializer_class = CahiertexteSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        """
        Filtrage des cahiers selon les paramètres fournis dans l'URL.
        """
        queryset = Cahiertexte.objects.all()
        classe = self.request.query_params.get('classe', None)
        date = self.request.query_params.get('date', None)
        professeur = self.request.query_params.get('professeur', None)

        if classe:
            queryset = queryset.filter(id_classe__id=classe)
        if date:
            queryset = queryset.filter(date_de_creation=date)
        if professeur:
            queryset = queryset.filter(id_classe__professeur__id=professeur)

        return queryset

    @extend_schema(tags=["Cahier-de-texte"])
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)


class CahierTexteAPIView(APIView):

    @extend_schema(tags=["Cahier-de-texte"])
    def get(self, request):
        cahiers = Cahiertexte.objects.all()  # Récupere tous les cahiers de texte
        serializer = CahiertexteSerializer(cahiers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CahierTexteDataAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(tags=["Cahier-de-texte"])
    def get(self, request, cahier_id):
        try:
            # Récupération du cahier de texte
            cahier = Cahiertexte.objects.get(pk=cahier_id)
            ues = Ue.objects.filter(classe=cahier.id_classe)
            seances = Seance.objects.filter(id_classe=cahier.id_classe)
        except Cahiertexte.DoesNotExist:
            return Response({"error": "Cahier de texte non trouvé"}, status=status.HTTP_404_NOT_FOUND)
        except Ue.DoesNotExist:
            return Response({"error": "Aucune UE trouvée pour cette classe"}, status=status.HTTP_404_NOT_FOUND)

        # Construction de la réponse JSON
        response_data = {
            "classe": {
                "nom": cahier.id_classe.nom_licence,
                "departement": cahier.id_classe.departement,
                "niveau": cahier.id_classe.niveau,
            },
            "ues": [
                {
                    "code": ue.code_ues,
                    "intitule": ue.intitule_ues,
                    "seances": [
                        {
                            "id": seance.id_seance,
                            "date_heure": seance.date_heure,
                            "contenu": seance.sous_session_seance,
                            "statut": "validé" if Validation.objects.filter(id_seance=seance,
                                                                            statut="validé").exists() else "non validé",
                            "validation": {
                                "statut": validation.statut,
                                "date_validation": validation.date_validation,
                                "signature": validation.id_professeur.signature.url if validation.statut == "validé" else "La séance n’a pas encore été validée par le professeur."
                            } if (validation := Validation.objects.filter(id_seance=seance).first()) else None,
                        }
                        for seance in Seance.objects.filter(id_classe=cahier.id_classe, id_ue=ue)
                    ],
                }
                for ue in ues
            ]
        }

        return Response(response_data, status=status.HTTP_200_OK)



"""@extend_schema(
    request=SeanceDetailsSerialiser,
    responses=SeanceDetailsSerialiser,
)"""


class SeanceDetailsView(APIView):
    serializer_class = SeanceDetailsSerialiser
    #permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        parameters=[
            OpenApiParameter("mention", str, OpenApiParameter.PATH, description="mention"),
            OpenApiParameter("nom_classe", str, OpenApiParameter.PATH, description="Class name"),
            OpenApiParameter("code_ue", str, OpenApiParameter.PATH, description="UE code"),

        ],
        tags=["Seances-de-classe"]
    )
    def get(self, request, mention, nom_classe, code_ue):

        serializer = self.serializer_class(data={"mention":mention, "nom_classe":nom_classe, "code_ue":code_ue})
        serializer.is_valid(raise_exception=True)

        ue = serializer.validated_data.get("ue")
        classe = serializer.validated_data.get("classe")
        data = {
            "seances":
            {
                "id": seance.id_seance,
                "date_heure": seance.date_heure,
                "contenu": seance.sous_session_seance,
                "statut": "validé" if Validation.objects.filter(id_seance=seance,
                                                                statut="validé").exists() else "non validé",
                "validation": {
                    "statut": validation.statut,
                    "date_validation": validation.date_validation,
                    "signature": validation.id_professeur.signature.url if validation.statut == "validé" else "La séance n’a pas encore été validée par le professeur."
                } if (validation := Validation.objects.filter(id_seance=seance).first()) else None,
            }
            for seance in Seance.objects.filter(id_classe=classe, id_ues=ue)
        }
        if not data:
            data = {"message": f"there is no seance for UE {ue} "}

        return Response(data, status=status.HTTP_200_OK)
#good
class SeanceCreateView(generics.CreateAPIView):
    serializer_class = SeanceCreateSerializer
    #permission_classes = [permissions.IsAuthenticated]



    @extend_schema(tags=["Seances-de-classe"])
    def post(self, request, *args, **kwargs):


        serializer = SeanceCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED) #to see later

# good but not sure if it is working , self.get_object ???
class SeanceUpdateView(generics.UpdateAPIView):
    queryset = Seance.objects.all()
    serializer_class = SeanceSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["patch"]


    @extend_schema(tags=["Seances-de-classe"])
    def patch(self, request, *args, **kwargs):
        instance = self.get_object()

        # Vérifier si la séance est validée
        validation = Validation.objects.filter(id_seance=instance).first()
        if validation and validation.statut == 'validé':
            # Autoriser uniquement la modification des chapitres pour les professeurs
            if request.user.role == 'Professeur':
                allowed_fields = ['sous_session_seance']

                for field in request.data.keys():
                    if field not in allowed_fields:
                        return Response(
                            {"detail": "Séance validée. Seul le contenu des chapitres peut être modifié."},
                            status=status.HTTP_403_FORBIDDEN
                        )
                """serializer = self.serializer_class(instance , data=request.data, partial=True)
                serializer.is_valid(raise_exception=True)
                self.perform_update(serializer)"""
                instance.sous_session_seance = request.data.get('sous_session_seance', instance.sous_session_seance)
                instance.save()
                return Response({"message": "Chapitres mis à jour avec succès."}, status=status.HTTP_200_OK)
            else:
                return Response(
                    {"detail": "Séance déjà validée. Modification interdite."},
                    status=status.HTTP_403_FORBIDDEN
                )
        else:
            return Response({"error":"Validation non trouvé "}, status=status.HTTP_404_NOT_FOUND)


# good but not sure if it is working , self.get_object ???
class SeanceDeleteView(generics.DestroyAPIView):
    queryset = Seance.objects.all()
    serializer_class = SeanceSerializer
    #permission_classes = [permissions.IsAuthenticated,]

    @extend_schema(tags=["Seances-de-classe"])
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()

        # Vérifier si la séance est validée
        validation = Validation.objects.filter(id_seance=instance).first()
        if validation and validation.statut == 'validé':
            # Seul un professeur ou un admin peut supprimer une séance validée
            if request.user.role not in ['Professeur', 'Admin']:
                return Response(
                    {"detail": "Suppression interdite. La séance est déjà validée."},
                    status=status.HTTP_403_FORBIDDEN
                )

        # Journalisation de la suppression , to see after
        print(f"Séance supprimée par {request.user.username} à {timezone.now()}")

        # Suppression de la séance
        return super().delete(request, *args, **kwargs)


class ValidationUpdateView(APIView):
    """
    Vue permettant à un professeur de valider une séance.
    """
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(tags=["Cahier-de-texte-validation-seances"])
    def patch(self, request, validation_id):
        try:
            # Récupérer la validation
            validation = Validation.objects.get(pk=validation_id)

            # Vérifier que l'utilisateur est le professeur associé
            if validation.id_professeur.user != request.user:
                return Response({"error": "Vous n'avez pas les droits pour valider cette séance."}, status=403)

            # Vérifier que le professeur a une signature
            if not validation.id_professeur.signature:
                return Response({"error": "Validation impossible : votre signature est absente."}, status=400)

            # Valider la séance
            validation.statut = "validé"
            validation.date_validation = timezone.now()
            validation.save()

            return Response({"message": "Séance validée avec succès.", "validation_id": validation.id_validation},
                            status=200)
        except Validation.DoesNotExist:
            return Response({"error": "Validation non trouvée."}, status=404)


class ValidationDeleteView(APIView):
    """
    Vue permettant de supprimer une validation (par professeur ou admin uniquement).
    """
    #permission_classes = [permissions.IsAuthenticated]

    @extend_schema(tags=["Cahier-de-texte-validation-seances"])
    def delete(self, request, validation_id):
        try:
            # Récupérer la validation
            validation = Validation.objects.get(pk=validation_id)

            # Vérifier les permissions : uniquement Professeur ou Admin
            if request.user.role not in ["Professeur", "Admin"]:
                return Response({"error": "Vous n'avez pas les droits pour supprimer cette validation."}, status=403)

            validation.delete()
            return Response({"message": "Validation supprimée avec succès."}, status=200)
        except Validation.DoesNotExist:
            return Response({"error": "Validation non trouvée."}, status=404)


class ValidationCahierAPIView(APIView):


    @extend_schema(tags=["Cahier-de-texte-validation-seances"])
    def post(self, request, cahier_id, prof_id):
        try:
            cahier = Cahiertexte.objects.get(pk=cahier_id)
            professeur = Professeur.objects.get(pk=prof_id)
        except (Cahiertexte.DoesNotExist, Professeur.DoesNotExist):
            return Response({"error": "Cahier ou professeur non trouvé"}, status=status.HTTP_404_NOT_FOUND)

        # Créer une validation avec la signature du professeur
        validation = Validation.objects.create(
            id_cahier=cahier,
            id_professeur=professeur,
            statut="validé",
            date_validation=request.data.get("date_validation"),
            signature=professeur.signature  # Récupère la signature associée
        )
        return Response(
            {"message": "Validation effectuée avec succès", "data": {"id_validation": validation.id_validation}},
            status=status.HTTP_201_CREATED)


class ListeValidationView(APIView):
    """
    Tableau de bord pour les professeurs.
    """
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(tags=["Cahier-de-texte-validation-seances"])
    def get(self, request):
        try:
            professeur = request.user.professeur

            # Récupérer toutes les validations liées au professeur
            validations = Validation.objects.filter(id_professeur=professeur)

            # Construction de la réponse
            dashboard_data = []

            # Parcourir les validations pour regrouper les données
            for validation in validations:
                cahier = validation.id_cahier
                ues = Ue.objects.filter(classe=cahier.id_classe)

                # Séparer les UEs validées et non validées
                ues_validées = [
                    {
                        "code": ue.code_ues,
                        "intitule": ue.intitule_ues,
                        "date_validation": Validation.objects.filter(id_ues=ue, statut="validé").first().date_validation
                    }
                    for ue in ues if Validation.objects.filter(id_ues=ue, statut="validé").exists()
                ]

                ues_non_validées = [
                    {
                        "code": ue.code_ues,
                        "intitule": ue.intitule_ues,
                    }
                    for ue in ues if not Validation.objects.filter(id_ues=ue, statut="validé").exists()
                ]

                # Ajouter les séances liées au cahier
                seances = Seance.objects.filter(id_cahier=cahier)
                seances_data = [
                    {
                        "id": seance.id_seance,
                        "date": seance.date_heure,
                        "contenu": seance.sous_session_seance,
                        "validation_statut": "validé" if Validation.objects.filter(id_seance=seance,
                                                                                   statut="validé").exists() else "non validé"
                    }
                    for seance in seances
                ]

                # Ajouter au tableau de bord
                dashboard_data.append({
                    "cahier_id": cahier.id_cahier,
                    "classe": {
                        "nom": cahier.id_classe.nom_licence,
                        "niveau": cahier.id_classe.niveau,
                        "departement": cahier.id_classe.departement
                    },
                    "ues_validées": ues_validées,
                    "ues_non_validées": ues_non_validées,
                    "seances": seances_data
                })

            return Response({"dashboard": dashboard_data}, status=200)

        except AttributeError:
            return Response({"error": "Vous n'êtes pas un professeur."}, status=403)






class ConvertHTMLToPDFView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(tags=["exportation-du-cahier-de-texte"])
    def post(self, request, *args, **kwargs):
        # Etape 1: Valider les données avec le serializer
        serializer = HTMLUploadSerializer(data=request.data)
        if serializer.is_valid():
            html_file = serializer.validated_data['file']

            # Etape 2: Lire le contenu du fichier HTML
            html_content = html_file.read().decode('utf-8')

            # Etape 3: Définir le chemin de stockage du PDF
            pdf_folder = os.path.join(settings.MEDIA_ROOT, 'pdfs')
            os.makedirs(pdf_folder, exist_ok=True)  # Créer le dossier s'il n'existe pas
            pdf_path = os.path.join(pdf_folder, f"{os.path.splitext(html_file.name)[0]}.pdf")
            # Etape 4: Convertir le HTML en PDF
            try:
                HTML(string=html_content).write_pdf(pdf_path)
            except Exception as e:
                return Response({"error": f"Erreur de conversion en PDF: {str(e)}"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            # Etape 5: Retourner le chemin du fichier PDF
            return Response({
                "message": "PDF généré avec succès",
                "pdf_path": f"{settings.MEDIA_URL}pdfs/{os.path.basename(pdf_path)}"
            }, status=status.HTTP_201_CREATED)
            # En cas d'erreur de validation
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class DownloadPDFView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(tags=["exportation-du-cahier-de-texte"])
    def get(self, request, filename):
        pdf_folder = os.path.join(settings.MEDIA_ROOT, 'pdfs')
        pdf_path = os.path.join(pdf_folder, filename)

        if not os.path.exists(pdf_path):
            return Response({"error": "Fichier non trouvé"}, status=status.HTTP_404_NOT_FOUND)

        # Retourne une réponse pour télécharger le fichier
        return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf', as_attachment=True, filename=filename)












#ues views




# -----------------------------------------ue -----------------------------------------------------------
# Vue pour lister et créer des UEs
# C'est juste pour tester l'upload du fichier de cours (un fichier de cours est associé à une UE)
# Peut etre modifié en cas de necessité
#class UeListCreateView(generics.ListCreateAPIView):
"""class UeListCreateView(generics.CreateAPIView):
    queryset = Ue.objects.all()
    serializer_class = UeSerializer
    #permission_classes = [permissions.IsAuthenticated]



    @extend_schema(tags=["UE"])
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def get(self, request, classe):
        pass



class UeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ue.objects.all()
    serializer_class = UeSerializer
    #permission_classes = [permissions.IsAuthenticated]

    @extend_schema(tags=["UE"])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    @extend_schema(tags=["UE"])
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(tags=["UE"])
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(tags=["UE"])
    def delete(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    def get_permissions(self):

        if self.request.method == 'POST':
            return [IsSecretaireClasse(), IsProfesseur(), IsCustomAdmin()]
        elif self.request.method == 'PUT':
            return [IsSecretaireClasse(), IsProfesseur(), IsCustomAdmin()]
        elif self.request.method == 'DELETE':
            return [IsSecretaireClasse(), IsProfesseur(), IsCustomAdmin()]

class ClasseListCreateView(generics.ListCreateAPIView):
    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(tags=["Classe"])
    def get(self, request, *args, **kwargs):
        
        return super().get(request, *args, **kwargs)

    @extend_schema(tags=["Classe"])
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)"""




# 🧩 LIST + CREATE UE
@extend_schema(tags=["UEs"])
class UeListCreateView(generics.ListCreateAPIView):
    serializer_class = UeSerializer
    queryset = Ue.objects.all()

    """def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [CanListUe]
        elif self.request.method == 'POST':
            permission_classes = [CanCreateUe]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [p() for p in permission_classes]"""

    @extend_schema(
        description="List all UEs of a given class (by nom_classe).",
        parameters=[],
        responses=UeSerializer(many=True),
    )
    def get(self, request, *args, **kwargs):
        nom_classe = kwargs.get('nom_classe')
        mention = kwargs.get('mention')
        classe = get_object_or_404(Classe, nom_licence=nom_classe, mention=mention)

        queryset = Ue.objects.filter(classe=classe)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @extend_schema(
        description="Create a UE linked to a specific class (by nom_classe).",
        request=UeSerializer,
        responses=UeSerializer,
    )
    def post(self, request, *args, **kwargs):
        nom_classe = kwargs.get('nom_classe')
        mention = kwargs.get('mention')
        classe = get_object_or_404(Classe, nom_licence=nom_classe, mention=mention)
        data = request.data.copy()
        data['classe'] = classe.id_classe
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 🧩 RETRIEVE + UPDATE + DELETE UE
@extend_schema(tags=["UEs"])
class UeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UeSerializer
    lookup_field = 'code_UEs'
    queryset = Ue.objects.all()

    """def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [CanRetrieveUe]
        elif self.request.method == 'PUT' or self.request.method == 'PATCH':
            permission_classes = [CanUpdateUe]
        elif self.request.method == 'DELETE':
            permission_classes = [CanDeleteUe]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [p() for p in permission_classes]"""






# -------------------------------------------fichier ue--------------------------------------------------



class FichierUeUploadAPIView(APIView):  # Permet l'upload des fichiers de cours
    parser_classes = (MultiPartParser, FormParser)  # Nécessaire pour gérer les fichiers avec FileField
    permission_classes = [IsProfesseur]

    @extend_schema(tags=["UE"])
    def post(self, request):
        serializer = FichierUeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FichierUeListAPIView(APIView):  # Permet de lister tous les fichiers de cours
    #delete

    @extend_schema(tags=["UE"])
    def get(self, request):
        fichiers_ue = Fichier_Ue.objects.all()
        serializer = FichierUeSerializer(fichiers_ue, many=True)
        return Response(serializer.data)

class FichierUeDetailAPIView(APIView):  # Permet d'accéder à un fichier spécifique

    @extend_schema(tags=["UE"])
    def get(self, request, id):
        try:
            fichier_ue = Fichier_Ue.objects.get(id_Fichiers_Ue=id)
            serializer = FichierUeSerializer(fichier_ue)
            return Response(serializer.data)
        except Fichier_Ue.DoesNotExist:
            return Response({"error": "Fichier non trouvé"}, status=status.HTTP_404_NOT_FOUND)


class FichierUeDeleteAPIView(APIView):  # Permet de supprimer un fichier spécifique
    permission_classes = [IsCustomAdmin | IsProfesseur]  # Seul le professeur ou l'admin peut supprimer un fichier

    @extend_schema(tags=["UE"])
    def delete(self, request, id):
        try:
            fichier_ue = Fichier_Ue.objects.get(id_Fichiers_Ue=id)
            fichier_ue.lien_fichier.delete()  # Supprime physiquement le fichier
            fichier_ue.delete()  # Supprime l'entrée dans la base de données
            return Response({"message": "Fichier supprimé avec succès"}, status=status.HTTP_204_NO_CONTENT)
        except Fichier_Ue.DoesNotExist:
            return Response({"error": "Fichier non trouvé"}, status=status.HTTP_404_NOT_FOUND)


# ----------------------------------------------Cahier de texte---------------------------------------------------------






"""class ScheduleView(APIView):
    #permission_classes = [permissions.IsAuthenticated]

    @extend_schema(tags=["UE"])
    def get(self,request,  classe_id):
        classe = get_object_or_404(Classe, id=classe_id)

        ue_list = Ue.objects.filter(classe=classe)
        data = {}

        for ue in ue_list:
            data[ue.code_UEs] = {"crenaux":ue.crenaux}

        return Response(data, status=status.HTTP_200_OK)

    def post(self, request, nom_classe):
        c"""

@extend_schema(tags=["Emploi-du-temps"])
class ClasseScheduleView(generics.GenericAPIView):
    serializer_class = ClasseScheduleSerializer

    @extend_schema(
        description="Get the schedule (PDF) of a class by its name (nom_licence).",
        responses=ClasseScheduleSerializer,
    )
    def get(self, request, *args, **kwargs):
        nom_classe = kwargs.get("nom_classe")
        classe = get_object_or_404(Classe, nom_licence=nom_classe)
        serializer = self.get_serializer(classe)
        return Response(serializer.data)

    @extend_schema(
        description="Upload or update the schedule (PDF) of a class by its name (nom_licence).",
        request=ClasseScheduleSerializer,
        responses=ClasseScheduleSerializer,
    )
    def put(self, request, *args, **kwargs):
        nom_classe = kwargs.get("nom_classe")
        classe = get_object_or_404(Classe, nom_licence=nom_classe)

        serializer = self.get_serializer(classe, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)




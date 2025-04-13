import os
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView
from django.conf import settings
from weasyprint import HTML
from .models import Ue, Fichier_Ue
from .serializers import UeSerializer, FichierUeSerializer, HTMLUploadSerializer
from accounts.permissions import IsProfesseur, IsCustomAdmin


# -----------------------------------------ue -----------------------------------------------------------
# Vue pour lister et créer des UEs
# C'est juste pour tester l'upload du fichier de cours (un fichier de cours est associé à une UE)
# Peut etre modifié en cas de necessité
class UeListCreateView(generics.ListCreateAPIView):
    queryset = Ue.objects.all()
    serializer_class = UeSerializer


# -------------------------------------------fichier ue--------------------------------------------------


class FichierUeListAPIView(APIView):  # Permet de lister tous les fichiers de cours

    def get(self, request):
        fichiers_ue = Fichier_Ue.objects.all()
        serializer = FichierUeSerializer(fichiers_ue, many=True)
        return Response(serializer.data)


class FichierUeUploadAPIView(APIView):  # Permet l'upload des fichiers de cours
    parser_classes = (MultiPartParser, FormParser)  # Nécessaire pour gérer les fichiers avec FileField
    permission_classes = [IsProfesseur]

    def post(self, request):
        serializer = FichierUeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FichierUeDetailAPIView(APIView):  # Permet d'accéder à un fichier spécifique
    def get(self, request, id):
        try:
            fichier_ue = Fichier_Ue.objects.get(id_Fichiers_Ue=id)
            serializer = FichierUeSerializer(fichier_ue)
            return Response(serializer.data)
        except Fichier_Ue.DoesNotExist:
            return Response({"error": "Fichier non trouvé"}, status=status.HTTP_404_NOT_FOUND)


class FichierUeDeleteAPIView(APIView):  # Permet de supprimer un fichier spécifique
    permission_classes = [IsCustomAdmin | IsProfesseur]  # Seul le professeur ou l'admin peut supprimer un fichier

    def delete(self, request, id):
        try:
            fichier_ue = Fichier_Ue.objects.get(id_Fichiers_Ue=id)
            fichier_ue.lien_fichier.delete()  # Supprime physiquement le fichier
            fichier_ue.delete()  # Supprime l'entrée dans la base de données
            return Response({"message": "Fichier supprimé avec succès"}, status=status.HTTP_204_NO_CONTENT)
        except Fichier_Ue.DoesNotExist:
            return Response({"error": "Fichier non trouvé"}, status=status.HTTP_404_NOT_FOUND)


# ----------------------------------------------Cahier de texte---------------------------------------------------------

class ConvertHTMLToPDFView(APIView):
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







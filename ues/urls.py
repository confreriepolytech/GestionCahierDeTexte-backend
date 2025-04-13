from django.urls import path
from .views import (
    UeListCreateView,
    FichierUeListAPIView,
    FichierUeUploadAPIView,
    FichierUeDetailAPIView,
    FichierUeDeleteAPIView,
    ConvertHTMLToPDFView
)

urlpatterns = [
    # Routes pour les Unités d'Enseignement (UEs)
    path('liste/', UeListCreateView.as_view(), name='ue_list_create'),  # Liste et création des UE

    # Routes pour les fichiers liés aux UEs
    path('fichiers/', FichierUeListAPIView.as_view(), name='fichier_ue_list'),  # Lister tous les fichiers de cours
    path('fichiers/upload/', FichierUeUploadAPIView.as_view(), name='fichier_ue_upload'),  # Uploader un fichier
    path('fichiers/<int:id>/', FichierUeDetailAPIView.as_view(), name='fichier_ue_detail'),  # Détails d'un fichier spécifique
    path('fichiers/<int:id>/delete/', FichierUeDeleteAPIView.as_view(), name='fichier_ue_delete'),  # Supprimer un fichier

    # Fonctionnalité de conversion HTML -> PDF
    path('convert-html-to-pdf/', ConvertHTMLToPDFView.as_view(), name='convert-html-to-pdf'),
]

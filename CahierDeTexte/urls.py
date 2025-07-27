from django.urls import path
from .views import (
    CahiertexteCreateView,
    CahiertexteListView,
    CahierTexteAPIView,
    CahierTexteDataAPIView,
    ValidationCahierAPIView,
    DownloadPDFView, ScheduleView, ConvertHTMLToPDFView, FichierUeDeleteAPIView, FichierUeDetailAPIView,
    FichierUeUploadAPIView, FichierUeListAPIView, UeListCreateView, UeDetailView, ClasseListCreateView
)

urlpatterns = [
    path('create/', CahiertexteCreateView.as_view(), name='cahier-create'),
    path('list/', CahiertexteListView.as_view(), name='cahier-list'),
    path('', CahierTexteAPIView.as_view(), name='cahier-overview'),
    path('<int:classe_id>/data/', CahierTexteDataAPIView.as_view(), name='cahier-data'),
    path('<int:cahier_id>/validate/<int:prof_id>/', ValidationCahierAPIView.as_view(), name='validate-cahier'),
    path('download/<str:filename>/', DownloadPDFView.as_view(), name='pdf-download'),

    # Routes pour les Unités d'Enseignement (UEs)

    path('Ue/', UeListCreateView.as_view(), name='ue_list_create'),  # Liste et création des UE

    path('Ue/<int:pk>', UeDetailView.as_view(), name='ue_detail'),

    path('Classe/', ClasseListCreateView.as_view(), name='classe_list_create'),  # Liste et création des classe

    # Routes pour les fichiers liés aux UEs
    path('fichiers/', FichierUeListAPIView.as_view(), name='fichier_ue_list'),  # Lister tous les fichiers de cours
    path('fichiers/upload/', FichierUeUploadAPIView.as_view(), name='fichier_ue_upload'),  # Uploader un fichier
    path('fichiers/<int:id>/', FichierUeDetailAPIView.as_view(), name='fichier_ue_detail'),  # Détails d'un fichier spécifique
    path('fichiers/<int:id>/delete/', FichierUeDeleteAPIView.as_view(), name='fichier_ue_delete'),  # Supprimer un fichier

    # Fonctionnalité de conversion HTML -> PDF
    path('convert-html-to-pdf/', ConvertHTMLToPDFView.as_view(), name='convert-html-to-pdf'),

    # feature schedule for ue
    path('emploi-du-temps/<int:classe_id>/', ScheduleView.as_view(), name='schedule'),

]

from django.urls import path
from .views import (
    CahiertexteCreateView,
    CahiertexteListView,
    CahierTexteAPIView,
    CahierTexteDataAPIView,
    ValidationCahierAPIView,
    DownloadPDFView, ConvertHTMLToPDFView, FichierUeDeleteAPIView, FichierUeDetailAPIView,
    FichierUeUploadAPIView, FichierUeListAPIView,  # UeListCreateView, UeDetailView, ClasseListCreateView,
    SeanceCreateView, SeanceUpdateView, SeanceDeleteView, ValidationUpdateView, ValidationDeleteView,
    ListeValidationView, SeanceDetailsView, ClasseScheduleView, UeListCreateView, UeDetailView
)

urlpatterns = [
    path('cahier-de-texte/create/', CahiertexteCreateView.as_view(), name='cahier-create'),
    #path('cahier-de-texte/list/', CahiertexteListView.as_view(), name='cahier-list'),
    #path('cahier-de-texte/data', CahierTexteAPIView.as_view(), name='cahier-overview'),
    path('cahier-de-texte/<int:classe_id>/data/', CahierTexteDataAPIView.as_view(), name='cahier-data'),
    #path('cahier-de-texte/<int:cahier_id>/validate/<int:prof_id>/', ValidationCahierAPIView.as_view(), name='validate-cahier'),
    path('cahier-de-texte/validation-update/<int:validation_id>', ValidationUpdateView.as_view(), name='validation-update'),
    path('cahier-de-texte/validation-delete/<int:validation_id>', ValidationDeleteView.as_view(), name='validation-delete'),
    path('cahier-de-texte/liste-validation-professeur/', ListeValidationView.as_view(), name='Liste-validation-profeseur'),
    # Route for seances
    path('seance-creation/', SeanceCreateView.as_view(), name='seance-creation'),
    path('<str:mention>-<str:nom_classe>/<str:code_ue>/seance-details', SeanceDetailsView.as_view(), name="seance-details"),
    #path('seance-details', SeanceDetailsView.as_view(), name="seance-details"),
    path('seance-update/', SeanceUpdateView.as_view(), name='seance-update'),
    path('seance-delete/<int:pk>/', SeanceDeleteView.as_view(), name='seance-deletion'),


    path('download/<str:filename>/', DownloadPDFView.as_view(), name='pdf-download'),

    # Routes pour les Unités d'Enseignement (UEs)

    #path('ue/', UeListCreateView.as_view(), name='ue_list_create'),  # Liste et création des UE

    #path('ue/<int:pk>', UeDetailView.as_view(), name='ue_detail'),

    #path('classe/', ClasseListCreateView.as_view(), name='classe_list_create'),  # Liste et création des classe

    # Routes pour les fichiers liés aux UEs
    #path('ue/fichiers/', FichierUeListAPIView.as_view(), name='fichier_ue_list'),  # Lister tous les fichiers de cours
    path('ue/fichiers/upload/', FichierUeUploadAPIView.as_view(), name='fichier_ue_upload'),  # Uploader un fichier
    path('ue/fichiers/<int:id>/', FichierUeDetailAPIView.as_view(), name='fichier_ue_detail'),  # Détails d'un fichier spécifique
    path('ue/fichiers/<int:id>/delete/', FichierUeDeleteAPIView.as_view(), name='fichier_ue_delete'),  # Supprimer un fichier

    # Fonctionnalité de conversion HTML -> PDF
    path('convert-html-to-pdf/', ConvertHTMLToPDFView.as_view(), name='convert-html-to-pdf'),

    # feature schedule for ue
    path('classes/<str:nom_classe>/schedule/', ClasseScheduleView.as_view(), name='classe-schedule'),
    path('classes/<str:mention>-<str:nom_classe>/ues/', UeListCreateView.as_view(), name='ue-list-create'),
    path('ues/<str:mention>-<str:code_UEs>/', UeDetailView.as_view(), name='ue-detail')

]

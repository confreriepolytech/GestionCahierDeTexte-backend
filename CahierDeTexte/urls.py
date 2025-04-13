from django.urls import path
from .views import (
    CahiertexteCreateView,
    CahiertexteListView,
    CahierTexteAPIView,
    CahierTexteDataAPIView,
    ValidationCahierAPIView,
    DownloadPDFView
)

urlpatterns = [
    path('create/', CahiertexteCreateView.as_view(), name='cahier-create'),
    path('list/', CahiertexteListView.as_view(), name='cahier-list'),
    path('', CahierTexteAPIView.as_view(), name='cahier-overview'),
    path('<int:classe_id>/data/', CahierTexteDataAPIView.as_view(), name='cahier-data'),
    path('<int:cahier_id>/validate/<int:prof_id>/', ValidationCahierAPIView.as_view(), name='validate-cahier'),
    path('download/<str:filename>/', DownloadPDFView.as_view(), name='pdf-download'),
]

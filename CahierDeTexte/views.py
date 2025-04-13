
import os
from django.utils import timezone
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from django.http import FileResponse
from GestionCahierDeTexte import settings
from .serializers import CahiertexteSerializer, SeanceSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Cahiertexte, Validation, Seance
from ues.models import  Ue
from accounts.models import Professeur


class IsSecretary(permissions.BasePermission):
    """
    Permission pour les secrétaires uniquement.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.groups.filter(name='secretaire').exists()


class CahiertexteCreateView(generics.CreateAPIView):
    """
    Vue pour créer un cahier de texte.
    Accessible uniquement aux secrétaires.
    """
    queryset = Cahiertexte.objects.all()
    serializer_class = CahiertexteSerializer
    permission_classes = [permissions.IsAuthenticated, IsSecretary]


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
        queryset = self.queryset
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


class CahierTexteAPIView(APIView):
    def get(self, request):
        cahiers = Cahiertexte.objects.all()  # Récupere tous les cahiers de texte
        serializer = CahiertexteSerializer(cahiers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CahierTexteDataAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

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


class SeanceCreateView(generics.CreateAPIView):
    serializer_class = SeanceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # Récupérer l'ID du cahier
        cahier_id = request.data.get('cahier')
        cahier = get_object_or_404(Cahiertexte, id=cahier_id)

        # Vérification des doublons pour la classe, date, et UE
        date = request.data.get("date")
        id_ue = request.data.get("id_ue")
        if Seance.objects.filter(id_classe=cahier.id_classe, id_ue=id_ue, date_heure=date).exists():
            return Response(
                {"detail": "Une séance pour cette classe, UE, et date existe déjà."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Données de la séance
        seance_data = {
            "cahier": cahier.id,
            "date_heure": date,
            "sous_session_seance": request.data.get("contenu"),
            "id_professeur": request.data.get("professeur"),
            "id_ue": id_ue,
            "id_classe": cahier.id_classe.id,
        }

        serializer = SeanceSerializer(data=seance_data)
        serializer.is_valid(raise_exception=True)
        seance = serializer.save()

        # Création automatique de la validation
        Validation.objects.create(
            id_cahier=cahier,
            id_professeur=seance.id_professeur,
            id_ues=seance.id_ue,
            id_seance=seance,
            statut="non validé"
        )

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SeanceUpdateView(generics.UpdateAPIView):
    queryset = Seance.objects.all()
    serializer_class = SeanceSerializer
    permission_classes = [permissions.IsAuthenticated]

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
                instance.sous_session_seance = request.data.get('sous_session_seance', instance.sous_session_seance)
                instance.save()
                return Response({"message": "Chapitres mis à jour avec succès."}, status=status.HTTP_200_OK)
            else:
                return Response(
                    {"detail": "Séance déjà validée. Modification interdite."},
                    status=status.HTTP_403_FORBIDDEN
                )

        # Permettre les autres modifications pour les séances non validées
        return super().patch(request, *args, **kwargs)


class SeanceDeleteView(generics.DestroyAPIView):
    queryset = Seance.objects.all()
    serializer_class = SeanceSerializer
    permission_classes = [permissions.IsAuthenticated]

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

        # Journalisation de la suppression
        print(f"Séance supprimée par {request.user.username} à {timezone.now()}")

        # Suppression de la séance
        return super().delete(request, *args, **kwargs)


class ValidationUpdateView(APIView):
    """
    Vue permettant à un professeur de valider une séance.
    """
    permission_classes = [permissions.IsAuthenticated]

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
    permission_classes = [permissions.IsAuthenticated]

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


class DownloadPDFView(APIView):
    def get(self, request, filename):
        pdf_folder = os.path.join(settings.MEDIA_ROOT, 'pdfs')
        pdf_path = os.path.join(pdf_folder, filename)

        if not os.path.exists(pdf_path):
            return Response({"error": "Fichier non trouvé"}, status=status.HTTP_404_NOT_FOUND)

        # Retourne une réponse pour télécharger le fichier
        return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf', as_attachment=True, filename=filename)

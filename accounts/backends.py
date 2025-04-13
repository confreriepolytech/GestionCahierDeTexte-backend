# backends.py
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.admin import User

from .models import SecretaireClasse, SecretaireGeneral, Professeur
import logging
logger = logging.getLogger(__name__)


class MultiUserAuthBackend:
    def authenticate(self, request, email=None, password=None):

        user_models = [
            SecretaireClasse,
            SecretaireGeneral,
            Professeur,
            User  # Inclut le modèle User par défaut (auth.User)
        ]
        # Vérifie l'email dans les 3 tables
        for user_model in user_models:
            try:
                user = user_model.objects.get(email=email)
                if check_password(password, user.password):
                    return user  # Retourne l'instance du modèle (User1, User2 ou User3)
            except user_model.DoesNotExist:
                continue
        return None

    def get_user(self, user_id):
        user_models = [
            SecretaireClasse,
            SecretaireGeneral,
            Professeur,
            User  # Inclut le modèle User par défaut (auth.User)
        ]
        # Cherche l'utilisateur dans les 3 tables
        for user_model in user_models:
            try:
                return user_model.objects.get(pk=user_id)
            except user_model.DoesNotExist:
                continue
        return None
from rest_framework.test import APITestCase
from django.urls import reverse

from accounts.models import Classe


class TestSetup(APITestCase):

    def setUp(self):
        self.register_url = reverse('user-registration')
        self.login_url = reverse('user-login')

        self.user_professeur_data= {
            'email':'test1_professeur@gmail.com',
            'password': 'test1_professeur_password',
            'nom':'test1_nom_professeur',
            'prenom':'test1_prenom_professeur',
            'role':'professeur'
        }

        Classe.objects.create(nom_licence='GE_S6',
                              mention='LF',
                              departement='GE',
                              niveau='Licence')
        print(Classe.objects.all().count())

        self.user_secretaire_classe_data = {
            'email': 'test1_secretaire_classe@gmail.com',
            'password': 'test1_secretaire_classe_password',
            'nom': 'test1_nom_secretaire_classe',
            'prenom': 'test1_prenom_secretaire_classe',
            'role': 'secretaire_classe',
            'classe':'GE_S6'
        }

        self.user_secretaire_general_data = {
            'email': 'test1_secretaire_general@gmail.com',
            'password': 'test1_secretaire_generalpassword',
            'nom': 'test1_nom_secretaire_general',
            'prenom': 'test1_prenom_secretaire_general',
            'role': 'secretaire_general',
            'departement':'GE'
        }
        self.user_secretaire_general_without_departement = {
            'email': 'test2_secretaire_general@gmail.com',
            'password': 'test2_secretaire_generalpassword',
            'nom': 'test2_nom_secretaire_general',
            'prenom': 'test2_prenom_secretaire_general',
            'role': 'secretaire_general',
        }

        return super().setUp()

    def Teardown(self):
        return super().tearDown()
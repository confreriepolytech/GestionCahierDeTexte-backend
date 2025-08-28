from rest_framework.test import APITestCase
from django.urls import reverse

from accounts.models import Classe


class TestSetup(APITestCase):

    def setUp(self):
        self.register_url = reverse('user-registration')
        self.login_url = reverse('user-login')
        self.logout_url = reverse('user-logout')


        self.user_professeur_data= {
            'email':'test1_professeur@gmail.com',
            'password': 'test1_professeur_password',
            'nom':'test1_nom_professeur',
            'prenom':'test1_prenom_professeur',
            'role':'professeur'
        }



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
        self.user_secretaire_general_with_fake_departement = {
            'email': 'test2_secretaire_general@gmail.com',
            'password': 'test2_secretaire_generalpassword',
            'nom': 'test2_nom_secretaire_general',
            'prenom': 'test2_prenom_secretaire_general',
            'role': 'secretaire_general',
            'departement':'fake departement '
        }
        self.user_secretaire_general_with_None_as_fake_departement = {
            'email': 'test2_secretaire_general@gmail.com',
            'password': 'test2_secretaire_generalpassword',
            'nom': 'test2_nom_secretaire_general',
            'prenom': 'test2_prenom_secretaire_general',
            'role': 'secretaire_general',
            'departement': 'None'
        }
        self.user_secretaire_general_with_blank_as_fake_departement = {
            'email': 'test2_secretaire_general@gmail.com',
            'password': 'test2_secretaire_generalpassword',
            'nom': 'test2_nom_secretaire_general',
            'prenom': 'test2_prenom_secretaire_general',
            'role': 'secretaire_general',
            'departement': ' '
        }

        #login
        self.user_professeur_login = {
            'email': 'test1_professeur@gmail.com',
            'password':'test1_professeur_password'
       }
        self.user_secretaire_general_login = {
            'email': 'test1_secretaire_general@gmail.com',
            'password':'test1_secretaire_generalpassword'
        }
        self.user_secretaire_classe_login = {
            'email': 'test1_secretaire_classe@gmail.com',
            'password': 'test1_secretaire_classe_password'
        }

        # login with invalid credential email

        self.user_professeur_login_invalid_credential_email = {
            'email': 'faketest1_professeur@gmail.com',
            'password': 'test1_professeur_password'
        }
        self.user_secretaire_general_login_invalid_credential_email = {
            'email': 'faketest1_secretaire_general@gmail.com',
            'password': 'test1_secretaire_generalpassword'
        }
        self.user_secretaire_classe_login_invalid_credential_email = {
            'email': 'faketest1_secretaire_classe@gmail.com',
            'password': 'test1_secretaire_classe_password'
        }

        #login with invalid password
        self.user_professeur_login_invalid_credential_password = {
            'email': 'test1_professeur@gmail.com',
            'password': 'faketest1_professeur_password'
        }
        self.user_secretaire_general_login_invalid_credential_password = {
            'email': 'test1_secretaire_general@gmail.com',
            'password': 'faketest1_secretaire_generalpassword'
        }
        self.user_secretaire_classe_login_invalid_credential_password = {
            'email': 'test1_secretaire_classe@gmail.com',
            'password': 'faketest1_secretaire_classe_password'
        }

        # login with invalid credentials (both , password dans username)
        self.user_professeur_login_invalid_credentials= {
            'email': 'faketest1_professeur@gmail.com',
            'password': 'faketest1_professeur_password'
        }
        self.user_secretaire_general_login_invalid_credentials = {
            'email': 'faketest1_secretaire_general@gmail.com',
            'password': 'faketest1_secretaire_generalpassword'
        }
        self.user_secretaire_classe_login_invalid_credentials = {
            'email': 'faketest1_secretaire_classe@gmail.com',
            'password': 'faketest1_secretaire_classe_password'
        }


        #-------------------logout----------------------------------
        self.user_professeur_logout_invalid_token = {
            'refresh_token':'fake token'
        }
        self.user_secretaire_general_logout_invalid_token = {
            'refresh_token': 'fake token'
        }
        self.user_secretaire_classe_logout_invalid_token = {
            'refresh_token': 'fake token'
        }








        return super().setUp()

    def Teardown(self):
        return super().tearDown()
from django.contrib.auth import get_user_model

from accounts.test.test_setup import TestSetup



User = get_user_model()




class TestRegistrationView(TestSetup):

    def test_user_cannot_register_with_no_data(self):
      response = self.client.post(self.register_url)

      self.assertEqual(response.status_code, 400)


    def test_user_professeur_can_register_with_data(self):
        response = self.client.post(self.register_url,
                                    self.user_professeur_data,
                                    format='json')

        self.assertEqual(response.status_code, 201)

    def test_user_secretaire_classe_can_register_with_data(self):
        response = self.client.post(self.register_url,
                                    self.user_secretaire_classe_data,
                                    format='json' )

        self.assertEqual(response.status_code, 201)


    def test_user_secretaire_general_can_register_with_data(self):
        response = self.client.post(self.register_url,
                                    self.user_secretaire_general_data,
                                    format='json' )
        self.assertEqual(response.status_code, 201)

    def test_user_secretaire_general_cannot_register_without_departement(self):
        response = self.client.post(self.register_url,
                                    self.user_secretaire_general_without_departement,
                                    format='json')

        self.assertEqual(response.status_code, 400)

    def test_user_secretaire_general_cannot_register_with_fake_departement(self):
        response = self.client.post(self.register_url,
                                    self.user_secretaire_general_with_fake_departement,
                                    format='json')

        self.assertEqual(response.status_code, 400)

    def test_user_secretaire_general_cannot_register_with_None_as_fake_departement(self):
        response = self.client.post(self.register_url,
                                    self.user_secretaire_general_with_None_as_fake_departement,
                                    format='json')

        self.assertEqual(response.status_code, 400)

    def test_user_secretaire_general_cannot_register_with_blank_as_departement(self):
        response = self.client.post(self.register_url,
                                    self.user_secretaire_general_with_blank_as_fake_departement,
                                    format='json')

        self.assertEqual(response.status_code, 400)




    """def test_user_cannot_register_with_another_account_name(self):
        response = self.client.post(self.register_url,
                                    self.user_another_account_name,
                                    format='json')
        import pdb
        pdb.set_trace()

        self.assertEqual(response.status_code, 400)"""











class TestLoginView(TestSetup):



    #Invalid credentials

    # invalid email
    def test_user_professeur_cannot_login_with_invalid_credential_email(self):

        response_create_user_professeur = self.client.post(self.register_url,
                                    self.user_professeur_data,
                                    format='json')
        response_login = self.client.post(self.login_url,
                                   self.user_professeur_login_invalid_credential_email,
                                   format='json')

        self.assertEqual(response_login.status_code, 401)

    def test_user_secretaire_general_cannot_login_with_invalid_credential_email(self):

        response_create_user_secretaire_genral = self.client.post(self.register_url,
                                    self.user_secretaire_general_data,
                                    format='json')
        response_login = self.client.post(self.login_url,
                                   self.user_secretaire_general_login_invalid_credential_email,
                                   format='json')


        self.assertEqual(response_login.status_code, 401)

    def test_user_secretaire_classe_cannot_login_with_invalid_credential_email(self):
        response_create_user_secretaire_classe = self.client.post(self.register_url,
                                                                  self.user_secretaire_classe_data,
                                                                  format='json')

        response_login = self.client.post(self.login_url,
                                          self.user_secretaire_classe_login_invalid_credential_email,
                                          format='json')
        self.assertEqual(response_login.status_code, 401)

    #invalid password
    def test_user_professeur_cannot_login_with_invalid_credential_password(self):
            response_create_user_professeur = self.client.post(self.register_url,
                                                               self.user_professeur_data,
                                                               format='json')
            response_login = self.client.post(self.login_url,
                                              self.user_professeur_login_invalid_credential_password,
                                              format='json')
            self.assertEqual(response_login.status_code, 401)

    def test_user_secretaire_general_cannot_login_with_invalid_credential_password(self):
            response_create_user_secretaire_genral = self.client.post(self.register_url,
                                                                      self.user_secretaire_general_data,
                                                                      format='json')
            response_login = self.client.post(self.login_url,
                                              self.user_secretaire_general_login_invalid_credential_password,
                                              format='json')

            self.assertEqual(response_login.status_code, 401)

    def test_user_secretaire_classe_cannot_login_with_invalid_credential_password(self):
            response_create_user_secretaire_classe = self.client.post(self.register_url,
                                                                      self.user_secretaire_classe_data,
                                                                      format='json')

            response_login = self.client.post(self.login_url,
                                              self.user_secretaire_classe_login_invalid_credential_password,
                                              format='json')


            self.assertEqual(response_login.status_code, 401)



    # both credentials are invalid(both, password and email)


    def test_user_professeur_cannot_login_with_invalid_credentials(self):

        response_login = self.client.post(self.login_url,
                                   self.user_professeur_login_invalid_credentials,
                                   format='json')

        self.assertEqual(response_login.status_code, 401)

    def test_user_secretaire_general_cannot_login_with_invalid_credentials(self):

        response_login = self.client.post(self.login_url,
                                   self.user_secretaire_general_login_invalid_credentials,
                                   format='json')


        self.assertEqual(response_login.status_code, 401)

    def test_user_secretaire_classe_cannot_login_with_invalid_credentials(self):

        response_login = self.client.post(self.login_url,
                                          self.user_secretaire_classe_login_invalid_credentials,
                                          format='json')

        self.assertEqual(response_login.status_code, 401)








    #credentials  are valid here

    # email is not verified
    def test_user_professeur_cannot_login_with_unverified_email(self):

        response_create_user_professeur = self.client.post(self.register_url,
                                    self.user_professeur_data,
                                    format='json')
        response_login = self.client.post(self.login_url,
                                   self.user_professeur_login,
                                   format='json')
        self.assertEqual(response_login.status_code, 401) #401 : UNAUTHORIZED

    def test_user_secretaire_general_cannot_login_with_unverified_email(self):

        response_create_user_secretaire_genral = self.client.post(self.register_url,
                                    self.user_secretaire_general_data,
                                    format='json')
        response_login = self.client.post(self.login_url,
                                   self.user_secretaire_general_login,
                                   format='json')


        self.assertEqual(response_login.status_code, 401) #401 : UNAUTHORIZED

    def test_user_secretaire_classe_cannot_login_with_unverified_email(self):
        response_create_user_secretaire_classe = self.client.post(self.register_url,
                                                                  self.user_secretaire_classe_data,
                                                                  format='json')

        response_login = self.client.post(self.login_url,
                                          self.user_secretaire_classe_login,
                                          format='json')


        self.assertEqual(response_login.status_code, 401)  # 401 : UNAUTHORIZED






    #verified email
    def test_user_professeur_can_login_with_verified_email(self):

        response_create_user_professeur = self.client.post(self.register_url,
                                    self.user_professeur_data,
                                    format='json')

        user = User.objects.get(email=response_create_user_professeur.data['email'])
        user.is_verified = True
        user.save(update_fields=['is_verified'])

        response_login = self.client.post(self.login_url,
                                   self.user_professeur_login,
                                   format='json')


        self.assertEqual(response_login.status_code, 200)

    def test_user_secretaire_general_can_login_with_verified_email(self):

        response_create_user_secretaire_general = self.client.post(self.register_url,
                                    self.user_secretaire_general_data,
                                    format='json')

        user = User.objects.get(email=response_create_user_secretaire_general.data['email'])
        user.is_verified = True
        user.save(update_fields=['is_verified'])

        response_login = self.client.post(self.login_url,
                                   self.user_secretaire_general_login,
                                   format='json')

        self.assertEqual(response_login.status_code, 200)

    def test_user_secretaire_classe_can_login_with_verified_email(self):
        response_create_user_secretaire_classe = self.client.post(self.register_url,
                                                                  self.user_secretaire_classe_data,
                                                                  format='json')

        user = User.objects.get(email=response_create_user_secretaire_classe.data['email'])
        user.is_verified = True
        user.save(update_fields=['is_verified'])

        response_login = self.client.post(self.login_url,
                                          self.user_secretaire_classe_login,
                                          format='json')


        self.assertEqual(response_login.status_code, 200)



    # account is disabled : is_active is False

    def test_user_professeur_cannot_login_with_disabled_account(self):
        response_create_user_professeur = self.client.post(self.register_url,
                                                           self.user_professeur_data,
                                                           format='json')

        user = User.objects.get(email=response_create_user_professeur.data['email'])

        user.is_verified = True
        user.is_active = False
        user.save()

        response_login = self.client.post(self.login_url,
                                          self.user_professeur_login,
                                          format='json')

        self.assertEqual(response_login.status_code, 401)

    def test_user_secretaire_general_cannot_login_with_disabled_account(self):
        response_create_user_secretaire_general = self.client.post(self.register_url,
                                                                   self.user_secretaire_general_data,
                                                                   format='json')

        user = User.objects.get(email=response_create_user_secretaire_general.data['email'])
        user.is_verified = True
        user.is_active = False
        user.save(update_fields=['is_active','is_verified'])

        response_login = self.client.post(self.login_url,
                                          self.user_secretaire_general_login,
                                          format='json')

        self.assertEqual(response_login.status_code, 401)

    def test_user_secretaire_classe_cannot_login_with_disabled_account(self):
        response_create_user_secretaire_classe = self.client.post(self.register_url,
                                                                  self.user_secretaire_classe_data,
                                                                  format='json')

        user = User.objects.get(email=response_create_user_secretaire_classe.data['email'])
        user.is_verified = True
        user.is_active = False
        user.save(update_fields=['is_active','is_verified'])

        response_login = self.client.post(self.login_url,
                                          self.user_secretaire_classe_login,
                                          format='json')

        self.assertEqual(response_login.status_code, 401)







class TestLogoutView(TestSetup):

    def test_user_cannot_logout_with_no_data(self):
        response_logout = self.client.post(self.logout_url,format='json')

        self.assertEqual(response_logout.status_code, 400)



    def test_user_professeur_cannot_logout_with_invalid_token(self):

        response_create_user_professeur = self.client.post(self.register_url,
                                                           self.user_professeur_data,
                                                           format='json')

        user = User.objects.get(email=response_create_user_professeur.data['email'])
        user.is_verified = True
        user.save(update_fields=['is_verified'])

        response_login = self.client.post(self.login_url,
                                          self.user_professeur_login,
                                          format='json')
        response_logout = self.client.post(self.logout_url,
                                           self.user_professeur_logout_invalid_token)


        self.assertEqual(response_logout.status_code, 400)

    def test_user_secretaire_classe_cannot_logout_with_invalid_token(self):
        response_create_user_secretaire_classe = self.client.post(self.register_url,
                                                           self.user_professeur_data,
                                                           format='json')

        user = User.objects.get(email=response_create_user_secretaire_classe.data['email'])
        user.is_verified = True
        user.save(update_fields=['is_verified'])

        response_login = self.client.post(self.login_url,
                                          self.user_professeur_login,
                                          format='json')
        response_logout = self.client.post(self.logout_url,
                                           self.user_secretaire_classe_logout_invalid_token)

        self.assertEqual(response_logout.status_code, 400)

    def test_user_secretaire_general_cannot_logout_with_invalid_token(self):

        response_create_user_secretaire_general = self.client.post(self.register_url,
                                                           self.user_professeur_data,
                                                           format='json')

        user = User.objects.get(email=response_create_user_secretaire_general.data['email'])
        user.is_verified = True
        user.save(update_fields=['is_verified'])

        response_login = self.client.post(self.login_url,
                                          self.user_professeur_login,
                                          format='json')
        response_logout = self.client.post(self.logout_url,
                                           self.user_secretaire_general_logout_invalid_token)

        self.assertEqual(response_logout.status_code, 400)


    def test_user_professeur_can_logout_with_valid_token(self):
        response_create_user_professeur = self.client.post(self.register_url,
                                                           self.user_professeur_data,
                                                           format='json')

        user = User.objects.get(email=response_create_user_professeur.data['email'])
        user.is_verified = True
        user.save(update_fields=['is_verified'])

        response_login = self.client.post(self.login_url,
                                          self.user_professeur_login,
                                          format='json')

        refresh_token = response_create_user_professeur.data['tokens']['refresh_token']

        import pdb
        pdb.set_trace()
        response_logout = self.client.post(self.logout_url,
                                           refresh_token,)

        self.assertEqual(response_logout.status_code, 400)

    def test_user_secretaire_classe_can_logout_with_valid_token(self):
        response_create_user_secretaire_classe = self.client.post(self.register_url,
                                                                  self.user_professeur_data,
                                                                  format='json')

        user = User.objects.get(email=response_create_user_secretaire_classe.data['email'])
        user.is_verified = True
        user.save(update_fields=['is_verified'])

        response_login = self.client.post(self.login_url,
                                          self.user_professeur_login,
                                          format='json')

        refresh_token = response_create_user_secretaire_classe.data.get('tokens')['refresh_token']
        response_logout = self.client.post(self.logout_url,
                                           refresh_token,)

        self.assertEqual(response_logout.status_code, 400)

    def test_user_secretaire_general_can_logout_with_valid_token(self):
        response_create_user_secretaire_general = self.client.post(self.register_url,
                                                                   self.user_professeur_data,
                                                                   format='json')

        user = User.objects.get(email=response_create_user_secretaire_general.data['email'])
        user.is_verified = True
        user.save(update_fields=['is_verified'])

        response_login = self.client.post(self.login_url,
                                          self.user_professeur_login,
                                          format='json')
        refresh_token = response_create_user_secretaire_general.data.get('tokens')['refresh_token']
        response_logout = self.client.post(self.logout_url,
                                           refresh_token,)

        self.assertEqual(response_logout.status_code, 400)
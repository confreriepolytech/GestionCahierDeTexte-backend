from accounts.test.test_setup import TestSetup


class TestViews(TestSetup):

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
                                    self.test_user_secretaire_general_cannot_register_without_departement,
                                    format='json')
        self.assertEqual(response.status_code, 400)
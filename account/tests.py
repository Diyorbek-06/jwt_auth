from multiprocessing.resource_tracker import register

from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.urls import reverse

# Create your tests here.


class AuthTest(APITestCase):
    def setUp(self):
        self.regis_url = reverse('register')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.test_url = reverse('test')

        self.user_data = {
            'username': 'user',
            'password': 'user'
        }

        self.client.post(self.regis_url, self.user_data)
        response = self.client.post(self.login_url, self.user_data)
        self.refresh_token = response.data['refresh']
        self.access_token = response.data['access']

    def test_regis(self):
        pass

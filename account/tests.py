from http.client import responses
from http.cookiejar import reach
from multiprocessing.resource_tracker import register

from django.template.context_processors import request
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
        data = {
            'username': 'user0',
            'password': 'user'
        }
        response = self.client.post(self.regis_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['data'], 'user0')
        self.assertEqual(response.data['msg'], "siz ro'yxat o'tdingiz")

    def test_login(self):
        response = self.client.post(self.login_url, self.user_data)



        self.assertEqual(response.status_code, 200)
        self.assertIn('refresh', response.data)
        self.assertIn('access' ,response.data)

    def test_logout(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.access_token)
        response = self.client.post(self.logout_url, {'refresh': self.refresh_token})

        self.assertEqual(response.data['msg'], "Tizimdan chiqdingiz")
        self.assertEqual(response.status_code, 200)
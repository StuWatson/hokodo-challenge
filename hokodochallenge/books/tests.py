from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class ListBookTests(APITestCase):

    def test_list_books(self):
        url = reverse('books')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

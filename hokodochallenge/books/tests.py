from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
import httpretty

class ListBookTests(APITestCase):

    def test_list_books(self):
        url = reverse('books')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_books_ordered_by_title(self):
        url = reverse('books')
        response = self.client.get(url + '?ordering=title')
        self.assertEqual(response.data[0]['title'], 'Designing Evolvable Web APIs with ASP.NET')
        self.assertEqual(response.data[9]['title'], 'You Don\'t Know JS')

        response = self.client.get(url + '?ordering=-title')
        self.assertEqual(response.data[0]['title'], 'You Don\'t Know JS')
        self.assertEqual(response.data[9]['title'], 'Designing Evolvable Web APIs with ASP.NET')


    def test_list_books_ordered_by_publish_date(self):
        url = reverse('books')
        response = self.client.get(url + '?ordering=published')
        self.assertEqual(response.data[0]['title'], 'Le père Goriot')
        self.assertEqual(response.data[9]['title'], 'Understanding ECMAScript 6')

        response = self.client.get(url + '?ordering=-published')
        self.assertEqual(response.data[0]['title'], 'Understanding ECMAScript 6')
        self.assertEqual(response.data[9]['title'], 'Le père Goriot')


    @httpretty.activate
    def test_endpoint_error(self):
        httpretty.register_uri(
            httpretty.GET,
            "https://hokodo-frontend-interview.netlify.com/data.json",
            body='Not found',
            status='500'
        )
        url = reverse('books')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertEqual(response.data, 'There was an error fetching the data - the service may be unavailable')


    @httpretty.activate
    def test_data_incorrect(self):
        httpretty.register_uri(
            httpretty.GET,
            "https://hokodo-frontend-interview.netlify.com/data.json",
            body='{"books": [{"book_name": "UnderstandingECMAScript 6"}]}',
            status='200'
        )
        url = reverse('books')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertEqual(response.data, 'There was an error reading the data - the format may have changed')

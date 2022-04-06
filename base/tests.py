import json
from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient, URLPatternsTestCase

from .models import Story

# Create your tests here.


class UserTest(APITestCase, URLPatternsTestCase):
    """ Test module for User """

    urlpatterns = [
        path('api/auth/', include('api.urls')),
    ]

    def setUp(self):
        self.story1 = Story.objects.create(
            title='QuickCheck is great!',
            text='go to quickcheck.com for more information',
            author='Daniel Olah',
        )

        self.story2 = Story.objects.create(
            title='Transdimensional space travel is impossible',
            text='admin',
            author='Daniel Olah'
        )

    def test_create(self):
        """ Test to create a Story """
        url = reverse('stories')
        data = {
            'title': 'Test Title',
            'text': 'lorem ipsum...',
            'author': 'Test author'
        }

        response = self.client.post(url, data)
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_data['success'], True)
        self.assertTrue('access' in response_data)

    def test_update(self):
        """ Test if a story can be updated """
        url = reverse('stories/3')
        data = {
            'title': 'Test Title',
            'text': 'Updated text!',
            'author': 'Test author'
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

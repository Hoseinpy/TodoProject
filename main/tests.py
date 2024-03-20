from rest_framework.test import APITestCase
from django.urls import reverse
from .models import TodoModel

class TodoAppTest(APITestCase):
    
    def test_add_todo_api(self):
        data = {'name': 'todo1', 'body': 'this is first todo', 'is_done': False}

        response = self.client.post(reverse('add-api'), data=data)
        self.assertEqual(response.status_code, 201)


class StatsTest(APITestCase):

    def test_stats_url(self):
        response = self.client.get(reverse('stats-api'))
        self.assertEqual(response.status_code, 200)

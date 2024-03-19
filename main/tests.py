from rest_framework.test import APITestCase
from django.urls import reverse

class TodoAppTest(APITestCase):
    
    def test_add_todo_api(self):
        data = {'name': 'todo1', 'body': 'this is first todo', 'is_done': False}

        response = self.client.post(reverse('add-api'), data=data)
        self.assertEqual(response.status_code, 201)
    
    
    def test_detail_todo_api(self):
        pass
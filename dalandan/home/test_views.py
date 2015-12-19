from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase


class ListTodoAPITest(APITestCase):
    fixtures = ['home_todos']

    def test_status(self):
        response = self.client.get(reverse('todos_api:list'))

        # 200 OK
        self.assertEqual(response.status_code, 200)

    def test_list(self):
        response = self.client.get(reverse('todos_api:list'))

        titles = [data['title'] for data in response.data]

        self.assertEqual(titles, [
            'Task #1',
            'Task #2',
            'Task #3',
        ])


class CreateTodoAPITest(APITestCase):

    @property
    def data(self):
        return {'title': 'Task #100'}

    def test_status(self):
        response = self.client.post(reverse('todos_api:create'), self.data)

        # 201 Created
        self.assertEqual(response.status_code, 201)

    def test_create(self):
        response = self.client.post(reverse('todos_api:create'), self.data)

        self.assertTrue(response.data['id'] > 0)

    def test_empty(self):
        response = self.client.post(reverse('todos_api:create'), {})

        # 400 Bad Request
        self.assertEqual(response.status_code, 400)


class UpdateTodoAPITest(APITestCase):
    fixtures = ['home_todos']

    def test_status(self):
        # Update task where ID = 1.
        url = reverse('todos_api:update', args=(1,))

        response = self.client.patch(url, {
            'status': 2
        })

        # 200 OK
        self.assertEqual(response.status_code, 200)

    def test_patch(self):
        """
        Update the status of the task where ID = 1.
        """
        url = reverse('todos_api:update', args=(1,))

        response = self.client.patch(url, {
            'status': 2
        })

        self.assertEqual(response.data['status'], 2)

    def test_put(self):
        """
        Update the title of the task where ID = 1.
        """
        url = reverse('todos_api:update', args=(1,))

        response = self.client.put(url, {
            'title': 'Task #1000'
        })

        self.assertEqual(response.data['title'], 'Task #1000')

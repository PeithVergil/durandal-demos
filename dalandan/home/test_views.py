from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase

from .models import Todo


class ListCreateTodoAPITest(APITestCase):
    fixtures = ['home_todos']

    @property
    def data(self):
        return {'title': 'Task #100'}

    def test_status_list(self):
        """
        Test the response status after a "GET" request.
        """
        response = self.client.get(reverse('todos_api:create'))

        # 200 OK
        self.assertEqual(response.status_code, 200)

    def test_list(self):
        response = self.client.get(reverse('todos_api:create'))

        titles = [data['title'] for data in response.data]

        self.assertEqual(titles, [
            'Task #1',
            'Task #2',
            'Task #3',
        ])

    def test_status_create(self):
        """
        Test the response status after a "POST" request.
        """
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


# class UpdateTodoAPITest(APITestCase):
#     fixtures = ['home_todos']

#     def test_status(self):
#         # Update task where ID = 1.
#         url = reverse('todos_api:retrieve', args=(1,))

#         response = self.client.patch(url, {
#             'status': 2
#         })

#         # 200 OK
#         self.assertEqual(response.status_code, 200)

#     def test_patch(self):
#         """
#         Update the status of the task where ID = 1.
#         """
#         url = reverse('todos_api:retrieve', args=(1,))

#         response = self.client.patch(url, {
#             'status': 2
#         })

#         self.assertEqual(response.data['status'], 2)

#     def test_put(self):
#         """
#         Update the title of the task where ID = 1.
#         """
#         url = reverse('todos_api:retrieve', args=(1,))

#         response = self.client.put(url, {
#             'title': 'Task #1000'
#         })

#         self.assertEqual(response.data['title'], 'Task #1000')


class RetrieveUpdateDeleteTodoAPITest(APITestCase):
    fixtures = ['home_todos']

    def test_status_retrieve(self):
        """
        Test the response status after a successful "GET" request.
        """
        response = self.client.get(reverse('todos_api:retrieve', args=(1,)))

        # 200 OK
        self.assertEqual(response.status_code, 200)

    def test_status_delete(self):
        """
        Test the response status after a successful "DELETE" request.
        """
        response = self.client.delete(reverse('todos_api:retrieve', args=(1,)))

        # 204 No Content
        self.assertEqual(response.status_code, 204)

    def test_status_patch(self):
        """
        Test the response status after a successful "PATCH" request.
        """
        url = reverse('todos_api:retrieve', args=(1,))

        response = self.client.patch(url, {
            'status': 2
        })

        # 200 OK
        self.assertEqual(response.status_code, 200)

    def test_status_put(self):
        """
        Test the response status after a successful "PUT" request.
        """
        url = reverse('todos_api:retrieve', args=(1,))

        response = self.client.put(url, {
            'title': 'Task #1000'
        })

        # 200 OK
        self.assertEqual(response.status_code, 200)

    def test_retrieve(self):
        """
        Retrieve the details of the task where ID = 1.
        """
        url = reverse('todos_api:retrieve', args=(1,))

        response = self.client.get(url)

        self.assertEqual(response.data['title'], 'Task #1')

    def test_delete(self):
        """
        Delete a task where ID = 1.
        """
        self.client.delete(reverse('todos_api:retrieve', args=(1,)))

        # The task should no longer exist.
        with self.assertRaises(Todo.DoesNotExist):
            Todo.objects.get(pk=1)

    def test_patch(self):
        """
        Patch the status of the task where ID = 1.
        """
        url = reverse('todos_api:retrieve', args=(1,))

        response = self.client.patch(url, {
            'status': 2
        })

        self.assertEqual(response.data['status'], 2)

    def test_put(self):
        """
        Update the title of the task where ID = 1.
        """
        url = reverse('todos_api:retrieve', args=(1,))

        response = self.client.put(url, {
            'title': 'Task #1000'
        })

        self.assertEqual(response.data['title'], 'Task #1000')

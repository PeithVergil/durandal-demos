from rest_framework.test import APITestCase

from .models import Todo
from .serializers import TodoSerializer


class TodoSerializerTest(APITestCase):

    fixtures = ['home_todos']

    def setUp(self):
        self.todo = Todo.objects.get(id=1)

    def create(self, data=None):
        if data is None:
            data = {}
        return TodoSerializer(data=data)

    def test_invalid_data(self):
        serializer = self.create()

        self.assertFalse(serializer.is_valid())

        self.assertEqual(serializer.errors, {
            'title': ['This field is required.']
        })

    def test_serializer_save(self):
        serializer = self.create({
            'title': 'Task #99'
        })

        self.assertTrue(serializer.is_valid())

        todo = serializer.save()

        # The primary key value has been assigned.
        self.assertTrue(todo.id > 0)

    def test_serializer_data(self):
        serializer = TodoSerializer(self.todo)

        self.assertEqual(serializer.data, {
            'id': 1,
            'title': 'Task #1',
            'status': 1,
            'date_created': '2015-11-30T06:14:07.208000Z',
            'date_updated': '2015-11-30T06:14:07.208000Z',
        })

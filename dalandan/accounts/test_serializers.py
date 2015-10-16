from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase

from .serializers import UserSerializer


User = get_user_model()


class UserSerializerTest(APITestCase):

    fixtures = ['accounts_users']

    def setUp(self):
        self.user = User.objects.get(username='peith')

    def create(self, data=None):
        if data is None:
            data = {}
        return UserSerializer(data=data)

    def test_invalid_data(self):
        serializer = self.create()

        self.assertFalse(serializer.is_valid())

        self.assertEqual(serializer.errors, {
            'username': ['This field is required.'],
            'password': ['This field is required.'],
        })

    def test_serializer_save(self):
        serializer = self.create({
            'username': 'hello',
            'password': 'world',
        })

        self.assertTrue(serializer.is_valid())
        
        serializer.save()

        user = User.objects.get(username='hello')

        self.assertTrue(user.id > 0)
        self.assertTrue(user.check_password('world'))
    
    def test_serializer_data(self):
        serializer = UserSerializer(self.user)

        self.assertEqual(serializer.data, {
            'username'    : 'peith',
            'date_created': '2015-09-16T15:17:03.932000Z',
            'date_updated': '2015-09-16T15:17:03.932000Z',
        })
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase


User = get_user_model()


class AuthMixin:

    fixtures = ['accounts_users']

    def authenticate(self, data=None):
        if data is None:
            data = {
                'username': 'peith',
                'password': 'abcdef',
            }

        return self.client.post('/accounts/auth/', data)


class AuthTest(AuthMixin, APITestCase):

    def test_valid_login(self):
        response = self.authenticate()

        # 200 OK
        self.assertEqual(response.status_code, 200)

    def test_invalid_login(self):
        # Wrong username and password.
        response = self.authenticate({
            'username': 'peith',
            'password': 'abcde',
        })

        # 400 BAD REQUEST
        self.assertEqual(response.status_code, 400)

    def test_verify_valid_token(self):
        auth = self.authenticate()

        response = self.client.post('/accounts/verify/', {
            'token': auth.data.get('token')
        })

        # 200 OK
        self.assertEqual(response.status_code, 200)

    def test_verify_invalid_token(self):
        token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ' \
                'lbWFpbCI6bnVsbCwiZXhwIjoxNDQyNDI0NDY1LCJ' \
                '1c2VybmFtZSI6InBlaXRoIiwidXNlcl9pZCI6MX0' \
                '.EFSgFLPMvumdCwqrt3-vQmWmflJkxiPTPV7pdBi' \
                'yJEQ'

        response = self.client.post('/accounts/verify/', {
            'token': token
        })

        # 400 BAD REQUEST
        self.assertEqual(response.status_code, 400)


class ListUserTest(AuthMixin, APITestCase):

    def test_list_user(self):
        response = self.client.get('/accounts/list/')

        # 200 OK
        self.assertEqual(response.status_code, 200)


class CreateUserTest(APITestCase):

    def setUp(self):
        self.url = reverse('accounts:create')

    def test_create(self):
        self.client.post(self.url, {
            'username': 'hello',
            'password': 'world',
            'password2': 'world',
        })

        user = User.objects.get(username='hello')

        self.assertTrue(user.id > 0)

    def test_redirect(self):
        """
        Redirect to the same page as the registration page.
        """
        response = self.client.post(self.url, {
            'username': 'hello',
            'password': 'world',
            'password2': 'world',
        })

        self.assertRedirects(response, self.url)


class RetrieveUserTest(AuthMixin, APITestCase):
    
    def test_retrieve_authenticated(self):
        result = self.authenticate()

        self.client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(result.data.get('token')))

        response = self.client.get('/accounts/me/')

        # 200 OK
        self.assertEqual(response.status_code, 200)

    def test_retrieve_unauthenticated(self):
        response = self.client.get('/accounts/me/')

        # 401 UNAUTHORIZED
        self.assertEqual(response.status_code, 401)
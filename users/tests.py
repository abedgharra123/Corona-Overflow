# type: ignore
from django.test import TestCase
import unittest 
from django.test import Client
from users.models import user

class UsersTest(TestCase):
    def setUp(self):
        user.objects.create(is_teacher=True)
    def test_user_model(self):
        us=user.objects.get(is_teacher=True)
        self.assertEqual(us.is_teacher,True)

class ViewsTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_users_list_view(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)


    def test_login_view(self):
        response = self.client.post('/login/',{'username':'tarek','password':'asd123asd123'},)
        self.assertEqual(response.status_code, 200)


    def test_register_view(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)

    def test_logout_view(self):
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 302)




if __name__ == '__main__':
    unittest.main()
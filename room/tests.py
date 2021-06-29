# type: ignore
from django.test import RequestFactory,TestCase
from django.contrib.auth.models import AnonymousUser, User
from django.test import Client
import room.views as views 
from room.models import room

from users.models import user

# Create your tests here.
class RoomsTest(TestCase):
    def setUp(self):
        room.objects.create(creator='yaseen',name='yasoon')
    def test_user_model(self):
        us=room.objects.get(creator='yaseen')
        self.assertEqual(us.name,'yasoon')

class ViewsAsTeacherTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.user = user.objects.create(username='teacher',email='aa@aga.sa',is_teacher=True)

    def test_update_view(self):
        request = self.factory.get('/home/update-room/')
        request.user = self.user
        response = views.create_room(request)
        self.assertEqual(response.status_code, 200)

    def test_create_view(self):
        request = self.factory.get('/home/create-room/')
        request.user = self.user
        response = views.create_room(request)
        self.assertEqual(response.status_code, 200)

    def test_delete_view(self):
        request = self.factory.get('/home/delete-room/')
        request.user = self.user
        response = views.create_room(request)
        self.assertEqual(response.status_code, 200)
        
class ViewsAsStudentTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.user = user.objects.create(username='student',email='aa@aga.sa',is_teacher=False)

    def test_update_view(self):
        request = self.factory.get('/home/update-room/')
        request.user = self.user
        response = views.create_room(request)
        self.assertEqual(response.status_code, 404)

    def test_create_view(self):
        request = self.factory.get('/home/create-room/')
        request.user = self.user
        response = views.create_room(request)
        self.assertEqual(response.status_code, 404)

    def test_delete_view(self):
        request = self.factory.get('/home/delete-room/')
        request.user = self.user
        response = views.create_room(request)
        self.assertEqual(response.status_code, 404)


class IntegrationTest(TestCase):
    def setUp(self):
        user.objects.create(username='teacher',email='aa@aga.sa',is_teacher=True)
        user.objects.create(username='student',email='aa@aa.sa',is_teacher=False)
        user.objects.create(username='admin',email='asa@aa.sa',is_superuser=True)
    def test_teacher_room(self):
        u = user.objects.get(username='teacher')
        r1 = room.objects.create(creator=u.username,name='teacher\'s room')
        self.assertEqual(u.is_teacher,True)
        self.assertNotEqual(r1, None)

    def test_student_room(self):
        u = user.objects.get(username='student')
        response = self.client.get('create-room')
        self.assertEqual(response.status_code, 404)
    
    def test_admin_room(self):
        u = user.objects.get(username='admin')
        r1 = room.objects.create(creator=u.username,name='admin\'s room')
        self.assertEqual(u.is_superuser,True)
        self.assertNotEqual(r1, None)

    
''' tests moudle '''
# pylint: disable=C0411,C0301,E1101,C0103
# type: ignore
from django.test import RequestFactory,TestCase
from django.test import Client
import room.views as views
from room.models import room
from blog.models import blog,answer
from users.models import user
''' setup function '''

class TestViewsAsTeacher(TestCase):
    ''' testing as teacher '''

    def setUp(self):
        ''' setup function '''

        room.objects.create(creator='yaseen',name='yasoon')
        self.factory = RequestFactory()
        self.client = Client()
        self.user = user.objects.create(username='teacher',email='aa@aga.sa',is_teacher=True)

    def test_inside_room(self):
        ''' inside room testing '''

        request = self.factory.get('inside-room')
        request.user = self.user
        response = views.create_room(request)
        self.assertEqual(response.status_code, 200)

    def test_update_blog(self):
        ''' update blog testing '''

        request = self.factory.get('update-blog')
        request.user = self.user
        response = views.create_room(request)
        self.assertEqual(response.status_code, 200)

    def test_delete_blog(self):
        ''' delete blog testing '''

        request = self.factory.get('delete-blog')
        request.user = self.user
        response = views.create_room(request)
        self.assertEqual(response.status_code, 200)

    def test_create_answer(self):
        ''' create answer testing '''

        request = self.factory.get('create-answer')
        request.user = self.user
        response = views.create_room(request)
        self.assertEqual(response.status_code, 200)

    def test_like_blog(self):
        ''' like blog testing '''

        request = self.factory.get('like-blog')
        request.user = self.user
        response = views.create_room(request)
        self.assertEqual(response.status_code, 200)

    def test_like_answer(self):
        ''' like answer testing '''

        request = self.factory.get('like-answer')
        request.user = self.user
        response = views.create_room(request)
        self.assertEqual(response.status_code, 200)

    def test_delete_answer(self):
        ''' delete answer testing '''

        request = self.factory.get('delete-answer')
        request.user = self.user
        response = views.create_room(request)
        self.assertEqual(response.status_code, 200)


class TestViewsAsStudent(TestCase):
    ''' testing as student '''

    def setUp(self):
        ''' setup function '''
        room.objects.create(creator='yaseen',name='yasoon')
        self.factory = RequestFactory()
        self.client = Client()
        self.user = user.objects.create(username='student',email='aa@aga.sa',is_teacher=False)

    def test_inside_room(self):
        ''' inside room testing '''
        request = self.factory.get('inside-room')
        request.user = self.user
        response = views.create_room(request)
        self.assertEqual(response.status_code, 404)

    def test_update_blog(self):
        ''' blog testing '''
        request = self.factory.get('update-blog')
        request.user = self.user
        response = views.create_room(request)
        self.assertEqual(response.status_code, 404)

    def test_delete_blog(self):
        ''' testing as blog '''
        request = self.factory.get('delete-blog')
        request.user = self.user
        response = views.create_room(request)
        self.assertEqual(response.status_code, 404)

    def test_create_answer(self):
        ''' create answer testing '''
        request = self.factory.get('create-answer')
        request.user = self.user
        response = views.create_room(request)
        self.assertEqual(response.status_code, 404)

    def test_like_blog(self):
        ''' testing as blog '''
        request = self.factory.get('like-blog')
        request.user = self.user
        response = views.create_room(request)
        self.assertEqual(response.status_code, 404)

    def test_like_answer(self):
        ''' answer testing '''
        request = self.factory.get('like-answer')
        request.user = self.user
        response = views.create_room(request)
        self.assertEqual(response.status_code, 404)

    def test_delete_answer(self):
        ''' answer testing '''
        request = self.factory.get('delete-answer')
        request.user = self.user
        response = views.create_room(request)
        self.assertEqual(response.status_code, 404)

class BlogTest(TestCase):
    ''' blog test '''
    def setUp(self):
        ''' setup function '''
        user.objects.create(is_teacher=True)
        blog.objects.create(creator=user.objects.get(is_teacher=True),question='question')
    def test_user_model(self):
        ''' user testing '''
        us=blog.objects.get(question='question')
        self.assertEqual(us.question,'question')

class AnswerTest(TestCase):
    ''' answer testing '''
    def setUp(self):
        ''' setup function '''
        user.objects.create(is_teacher=True)
        blog.objects.create(creator=user.objects.get(is_teacher=True),question='question')
        answer.objects.create(creator=user.objects.get(is_teacher=True),question=blog.objects.get(question='question'),answer='blabla')
    def test_user_model(self):
        ''' testing user model '''
        us=answer.objects.get(answer='blabla')
        self.assertEqual(us.answer,'blabla')

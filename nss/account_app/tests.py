#Last modified by César Buenfil on Oct 19,2018
from django.test import TestCase
from account_app.models import Profile
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
# Create your tests here.





##Pruebas Martín

class PruebaUsuario(TestCase):
    """docstring for PruebaUsuario."""
    def setUp(self):
        self.user1 = User.objects.create_user('user1', none, 'test1234')


class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'norco',
            'password': 'solecito'}
        User.objects.create_user(**self.credentials)
    def test_login(self):
        # send login data
        response = self.client.post('/user/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)


class CreateProject(TestCase):
    #You can not create a project if you are not login
    def test_view_not_login_create_project(self):
            response = self.client.post(reverse('project_app:create'))
            self.assertNotEquals(response.status_code, 200)
            # self.assertTemplateUsed(response, 'project_form.html')

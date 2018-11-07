#Last modified by César Buenfil on Oct 19,2018
from django.test import TestCase
from account_app.models import *
from project_app.models import *
import unittest
from django.test import Client
from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse
from . import views
from .models import *
from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase
from account_app.views import IndexView
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile
from account_app.forms import *
from django.core.validators import FileExtensionValidator
from django.core.validators import validate_image_file_extension
# Create your tests here.

class Navigation(TestCase):
    def setUp(self):
        self.client = Client()

    def test_navigate(self):
        response = self.client.get('/project_app/createProyecto/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'account_app/index.html')

    def test_home_page_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, 'TEEM')

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('project_app:create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project_app/project_form.html')

class CheckHelp(TestCase):
    def setUp(self):
        self.client = Client()

    def test_registerHelp(self):
        response = self.client.get('/user/registrar/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '150 characters')


class LogInOutTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.my_admin = User(username='user', is_staff=True)
        self.my_admin.set_password('passphrase') # can't set above because of hashing
        self.my_admin.save()

    def test_LogIn(self):
        loginresponse = self.client.login(username='user',password='passphrase')
        response=self.client.get('/admin/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(loginresponse) # should now return "true"

    def test_LogOut(self):
        loginresponse = self.client.login(username='user',password='passphrase')
        response=self.client.get('/admin/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/admin/logout/')
        self.assertFalse(response.context['user'].is_active)
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 302)

class PasswordHashing(TestCase):
    def setUp(self):
        self.client = Client()
        self.my_admin = User(username='user', password= 'passphrase')
        self.my_admin.save()

    def test_LogIn(self):
        loginresponse = self.client.login(username='user',password='passphrase')
        response=self.client.get('/admin/')
        self.assertEqual(response.status_code, 302)
        self.assertFalse(loginresponse) # should now return "true"


class VerificationTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='jacob', email='jacob@…', password='top_secret')

    def test_details(self):
        request = self.factory.get('index')
        request.user = self.user

        request.user = AnonymousUser()

        response = IndexView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def no_test_details(self):
        request = self.factory.get('home')
        request.user = self.user

        request.user = AnonymousUser()

        response = IndexView.as_view()(request)
        self.assertEqual(response.status_code, 404)

class UserAccounts(TestCase):
    # Function description: Set up for the testcase, create a superuser
    def setUp(self):
        # Create user
        self.user = User.objects.create_superuser(username='testuser2', email="example2@example.com",
                                                  password='pass2')
        self.user2 = User.objects.create_user(username='testuser1', email="example2@example.com",
                                              password='pass1')
        self.user.save()
        self.user2.save()

    def tearDown(self):
        del self.user
        del self.user2

    # Function description: assert it logs in as admin, make sure the user is able to see the list of users
    def test_logged_in_displays_users(self):
        self.client.login(username='testuser2', password='pass2')
        response = self.client.get('/admin/')

        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Site administration')
        response = self.client.get('/admin/logout/')
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['user'].is_active)

    def test_users_created(self):
        self.client.login(username='testuser2', password='pass2')
        response = self.client.get('/admin/auth/user/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testuser1')
        self.assertContains(response, 'testuser2')
        self.assertNotContains(response, 'testuser3')

class UserAccountsInfo(TestCase):
    # Function description: Set up for the testcase, create a superuser
    def setUp(self):
        # Create user
        self.user = User.objects.create_superuser(username='testuser1', email="example2@example.com",
                                                  password='pass1')
        self.useraux = UserProfileInfo.objects.create(user = self.user, profile_pic = SimpleUploadedFile(name='k.png', content=open('media/profile_pics/k.png', 'rb').read(), content_type='image/png'), portfolio_site = "Google.com")
        self.user.save()
        self.useraux.save()

    def tearDown(self):
        del self.user

    def test_validation(self):
        validate_image_file_extension(self.useraux.profile_pic)
        user_form = UserProfileInfoForm(data={'profile_pic': self.useraux.profile_pic, 'portfolio_site' : self.useraux.portfolio_site })
        self.assertTrue(user_form.is_valid())

    def test_users_created(self):
        self.client.login(username='testuser1', password='pass1')

        response = self.client.get('/admin/account_app/userprofileinfo/1/change/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Google.com")
        self.assertNotContains(response, 'testuser2')

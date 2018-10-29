from django.test import TestCase, RequestFactory

from django.urls import reverse, reverse_lazy
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User;
from account_app.models import Profile

# Create your tests here.

class CreateUpdateProfile(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.credentials = {
            'username': 'norco',
            'password': 'solecito'}
        User.objects.create_user(**self.credentials)
    def test_login(self):
        # send login data
        response = self.client.post('/user/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)
        
    def test_profile_while_not_auth(self):
        login = self.client.login(username='norco', password='solecito')
        username='norco'
        response = self.client.post(reverse('profiles_app:detail', args=[username]), self.credentials, follow=True)
        print (response.content)
        self.assertNotEquals(response.status_code, 200)


class SeeProfiles(object):
    """docstring forSeeProfiles."""

    def create_profiles(self):
        user=User.objects.create(username='norco', password='solecito')
        self.profile=Profile.objects.create( avatar='', bio='Esta es mi bio', link='http://toastdriven.com/blog/2011/apr/17/guide-to-testing-in-django-2/', user_id=user )
        return self.profile
    def test_see_profiles(self):
        create=self.create_profiles()
        response = self.client.get(reverse('profiles_app:'), follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "norco")

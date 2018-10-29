from django.test import TestCase, RequestFactory

from .models import project, category, location, rolInfo
from django.contrib.auth.models import User;
from django.urls import reverse, reverse_lazy
from django.template.defaultfilters import slugify
from .views import ProjectDetailView
# Create your tests here.
#
class ProjectTestCase(TestCase):
    def setUp(self):
        # self.project1= project.objects.create(pro_name='Micasa')
        project_category= category.objects.create(category='JOJO');
        project_location= location.objects.create(location='Marte');
        project_rol= rolInfo.objects.create(rol_name='Vendedor', rol_due_date='2018-10-12', rol_amount='3', rol_location = project_location)
        self.project1= project.objects.create(pro_name='Micasa',pro_description= 'Una cool casa',pro_video= 'https://www.youtube.com/watch?v=bdQhytHcZnY',pro_about_us= 'Somos creadores de casa', pro_phrase= 'casa casa',pro_creation_date= '2018-10-10', pro_category=project_category, pro_location=project_location)
        # self.project1.pro_roles.set(project_rol)
    def test_project_exist(self):
        exists = project.objects.filter(pro_name='Micasa').exists()
        self.assertEqual(exists, True)

class ProjectTestCase2(TestCase):
    def setUp(self):
        # self.project1= project.objects.create(pro_name='Micasa')
        project_category= category.objects.create(category='--');
        project_location= location.objects.create(location='´Compradoe');
        project_rol= rolInfo.objects.create(rol_name='Vendedor', rol_due_date='2018-10-12', rol_amount='1', rol_location = project_location)
        self.project1= project.objects.create(pro_name='sofa',pro_description= '',pro_video= 'https://www.youtube.com/watch?v=bdQhytHcZnY',pro_about_us= 'Somos creadores de casa', pro_phrase= 'casa casa',pro_creation_date= '2018-10-10', pro_category=project_category, pro_location=project_location)
        # self.project1.pro_roles.set(project_rol)
    def test_project_exist(self):
        exists = project.objects.filter(pro_name='sofa').exists()
        self.assertEqual(exists, True)

class ProjectTestCase3(TestCase):
    def setUp(self):
        # self.project1= project.objects.create(pro_name='Micasa')
        project_category= category.objects.create(category='');
        project_location= location.objects.create(location='´Nada');
        project_rol= rolInfo.objects.create(rol_name='Vendedor', rol_due_date='2018-10-12', rol_amount='1', rol_location = project_location)
        self.project1= project.objects.create(pro_name='',pro_description= '',pro_video= 'https://www.youtube.com/watch?v=bdQhytHcZnY',pro_about_us= 'Somos creadores de casa', pro_phrase= 'casa casa',pro_creation_date= '2018-10-10', pro_category=project_category, pro_location=project_location)
        # self.project1.pro_roles.set(project_rol)
    def test_project_exist(self):
        exists = project.objects.filter(pro_name=' Casa ').exists()
        self.assertEqual(exists, False)



class CreateProject(TestCase):
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
    def test_create_while_login(self):
        response = self.client.post(reverse('project_app:create'), self.credentials, follow=True)
        self.assertEquals(response.status_code, 200)

# class UpdateProject(TestCase):
#     def setUp(self):
#             self.credentials = {
#                 'username': 'norco',
#                 'password': 'solecito'}
#             User.objects.create_user(**self.credentials)
#             project_category= category.objects.create(category='--');
#             project_location= location.objects.create(location='´Compradoe');
#             project_rol= rolInfo.objects.create(rol_name='Vendedor', rol_due_date='2018-10-12', rol_amount='1', rol_location = project_location)
#             self.project1= project.objects.create(pro_name='nosofa',pro_description= '',pro_video= 'https://www.youtube.com/watch?v=bdQhytHcZnY',pro_about_us= 'Somos creadores de casa', pro_phrase= 'casa casa',pro_creation_date= '2018-10-10', pro_category=project_category, pro_location=project_location)
#             # self.project1.pro_roles.set(project_rol)
#     def test_project_exist(self):
#         exists = project.objects.filter(pro_name='nosofa').exists()
#         self.assertEqual(exists, True)
#
#     def test_login(self):
#         # send login data
#         response = self.client.post('/user/login/', self.credentials, follow=True)
#         # should be logged in now
#         self.assertTrue(response.context['user'].is_active)
#     def test_create_while_login(self):
#         login = self.client.login(username='norco', password='solecito')
#         # create=self.setUp()
#         response = self.client.post('/project_app/update/1/', follow=True)
#         print (response.content)
#         self.assertEquals(response.status_code, 200)
#         self.assertContains(response, "login")
#
#     def test_see_details(self):
#         #Sin pasar parámetros de content
#         result = self.client.post('/project_app/1/nosofa/')
#
#         # self.assertEquals(result.status_code, 200)
#         # self.assertContains(result, "nosofa")

class ProjectTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.credentials = {
            'username': 'norco',
            'password': 'solecito'}
        User.objects.create_user(**self.credentials)

    def create_project(self):
        project_category= category.objects.create(category='--');
        project_location= location.objects.create(location='´Compradoe');
        project_rol= rolInfo.objects.create(rol_name='Vendedor', rol_due_date='2018-10-12', rol_amount='1', rol_location = project_location)
        self.project1= project.objects.create(pro_name='nosofa',pro_description= '',pro_video= 'https://www.youtube.com/watch?v=bdQhytHcZnY',pro_about_us= 'Somos creadores de casa', pro_phrase= 'casa casa',pro_creation_date= '2018-10-10', pro_category=project_category, pro_location=project_location)
        # self.project1.pro_roles.set(project_rol)s
        return self.project1

    def test_project_exist(self):
        new_project=self.create_project()
        exists = project.objects.filter(pro_name='nosofa').exists()
        self.assertEqual(exists, True)

    def test_login(self):
        # send login data
        response = self.client.post('/user/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)

    def test_create_while_login(self):
        login = self.client.login(username='norco', password='solecito')
        create=self.create_project()
        response = self.client.post(reverse('project_app:create'), follow=True)
        # print (response.content)
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "create")

    def test_create_while_not_login(self):
        create=self.create_project()
        response = self.client.post(reverse('project_app:create'), follow=True)
        # print (response.content)
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "login")
        #Se prueba la redirección

##NO AUTHENTICATION
    def test_delete_project_not_auth(self):
    #     #Sin pasar parámetros de content
        create=self.create_project()
        # print(create.id)
        # print(create.pro_name)
        response=self.client.get(reverse_lazy('project_app:delete', args=[create.id]))
        # response=ProjectDetailView.as_view()(request)
        # print (response.content)
        self.assertNotEquals(response.status_code, 200)
        # self.assertContains(response, "nosofa")
#AUTHENTICATION
    def test_delete_project_auth(self):
        login = self.client.login(username='norco', password='solecito')
        create=self.create_project()
        # print(create.id)
        # print(create.pro_name)
        response=self.client.get(reverse_lazy('project_app:delete', args=[create.id]))
        # print (response.content)
        self.assertEquals(response.status_code, 200)
        # self.assertContains(response, "nosofa")

    def test_delete_project_auth_do(self):
        login = self.client.login(username='norco', password='solecito')
        create=self.create_project()
        # print(create.id)
        # print(create.pro_name)
        response=self.client.post(reverse_lazy('project_app:delete', args=[create.id]))
        print(response.content)
        #Redirect and delete
        self.assertEquals(response.status_code, 302)
        exists = project.objects.filter(pro_name='nosofa').exists()
        self.assertEqual(exists, False)

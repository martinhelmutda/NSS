from django.test import TestCase, RequestFactory

from project_app.models import project, category, location, rolInfo
from django.contrib.auth.models import User;
from project_app.forms import formProject, formProjectAddRol, formImg, rol_formset
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse, reverse_lazy
from django.template.defaultfilters import slugify
from .views import ProjectDetailView
# Create your tests here.
#

""" TESTS DE ANGIE """
#
# class createRol(object): ##Exitoso
#     def setUp(self):
#         rol_location= location.objects.create(location='Morelos');
#         rol= rolInfo.objects.create(rol_name='Periodista', rol_due_date='2018-10-10', rol_amount='2', rol_description='Tendrá que escribir mucho', rol_location = rol_location)
#     def test_createRol_exist(self):
#         self.assertEqual(rol, True)
#
# class createRol2(object): ##NO Exitoso, wrong date format
#     def setUp(self):
#         rol_location= location.objects.create(location='Morelos');
#         rol= rolInfo.objects.create(rol_name='Periodista', rol_due_date='10-10-2018', rol_amount='2', rol_description='Tendrá que escribir mucho', rol_location = rol_location)
#     def test_createRol_exist(self):
#         self.assertEqual(rol, False)
#
# class uploadImage(object):
#     def setUp(self):
#         category_cat=category.objects.create(category="emprendimiento")
#         location_loc= location.objects.create(location='Morelos');
#         rol= rolInfo.objects.create(rol_name='Periodista', rol_due_date='10-10-2018', rol_amount='2', rol_description='Tendrá que escribir mucho', rol_location = location_loc)
#
#         pro_pro = project.objects.create(pro_name='Pitch&Catch', pro_description='Es un evento de emprendimiento',
#                pro_video='https://www.youtube.com/watch?v=CcTl_ln4RNw',pro_about_us="Somos estudiantes",
#                 pro_phrase='es sin fines de lucro',pro_creation_date='2018-10-10', pro_category= category_cat,
#                  pro_location=location_loc, pro_roles=rol);
#         img= projectImg.objects.create(pro_img='nombre.png', pro=pro_pro)
#     def test_uploadImage_exist(self):
#         self.assertEqual(img, True)
#
# class uploadImage(object):
#     def setUp(self):
#         category_cat=category.objects.create(category="emprendimiento")
#         location_loc= location.objects.create(location='Morelos');
#         rol= rolInfo.objects.create(rol_name='Periodista', rol_due_date='10-10-2018', rol_amount='2', rol_description='Tendrá que escribir mucho', rol_location = location_loc)
#
#         pro_pro = project.objects.create(pro_name='Pitch&Catch', pro_description='Es un evento de emprendimiento',
#                pro_video='https://www.youtube.com/watch?v=CcTl_ln4RNw',pro_about_us="Somos estudiantes",
#                 pro_phrase='es sin fines de lucro',pro_creation_date='2018-10-10', pro_category= category_cat,
#                  pro_location=location_loc, pro_roles=rol);
#         img= projectImg.objects.create(pro_img='hola.jpg', pro=pro_pro)
#     def test_uploadImage_exist(self):
#         self.assertEqual(img, True)
#
# class uploadImage(object):
#     def setUp(self):
#         category_cat=category.objects.create(category="emprendimiento")
#         location_loc= location.objects.create(location='Morelos');
#         rol= rolInfo.objects.create(rol_name='Periodista', rol_due_date='10-10-2018', rol_amount='2', rol_description='Tendrá que escribir mucho', rol_location = location_loc)
#
#         pro_pro = project.objects.create(pro_name='Pitch&Catch', pro_description='Es un evento de emprendimiento',
#                pro_video='https://www.youtube.com/watch?v=CcTl_ln4RNw',pro_about_us="Somos estudiantes",
#                 pro_phrase='es sin fines de lucro',pro_creation_date='2018-10-10', pro_category= category_cat,
#                  pro_location=location_loc, pro_roles=rol);
#         img= projectImg.objects.create(pro_img='nombre.txt', pro=pro_pro)
#     def test_uploadImage_exist(self):
#         self.assertEqual(img, False)
#
# class createCategory(object):
#         def setUp(self):
#             pro_category= category.objects.create(category='Basketball');
#         def test_createCategory_exist(self):
#             self.assertEqual(rol, True)
#
# class createCategory(object):
#         def setUp(self):
#             pro_category= category.objects.create(category='');
#         def test_createCategory_exist(self):
#             self.assertEqual(rol, False)
#
# class testLabels(object):
#         def setUpTestData(cls):
#         # Set up non-modified objects used by all test methods
#         category_cat=category.objects.create(category="emprendimiento")
#         location_loc= location.objects.create(location='Morelos');
#         rol= rolInfo.objects.create(rol_name='Periodista', rol_due_date='10-10-2018', rol_amount='2', rol_description='Tendrá que escribir mucho', rol_location = location_loc)
#
#         pro_pro = project.objects.create(pro_name='Pitch&Catch', pro_description='Es un evento de emprendimiento',
#                pro_video='https://www.youtube.com/watch?v=CcTl_ln4RNw',pro_about_us="Somos estudiantes",
#                 pro_phrase='es sin fines de lucro',pro_creation_date='2018-10-10', pro_category= category_cat,
#                  pro_location=location_loc, pro_roles=rol);
#         img= projectImg.objects.create(pro_img='nombre.txt', pro=pro_pro)
#
#     def test_category_cat_label(self):
#         category = category.objects.get(id=1)
#         field_label = category._meta.get_field('category_cat').verbose_name
#         self.assertEquals(field_label, 'Categoría')
#
#     def test_location_label(self):
#         location = location.objects.get(id=1)
#         field_label = location._meta.get_field('location').verbose_name
#         self.assertEquals(field_label, 'Ubicación')
#
#     def test_rol_name_label(self):
#         rol_name = rolInfo.objects.get(id=1)
#         field_label = rolInfo._meta.get_field('rol_name').verbose_name
#         self.assertEquals(field_label, 'Nombre del puesto disponible')
#
#     def test_rol_due_date_label(self):
#         due_date = rolInfo.objects.get(id=1)
#         field_label = rolInfo._meta.get_field('rol_due_date').verbose_name
#         self.assertEquals(field_label, 'Fecha límite para aplicar')
#
#     def test_rol_amount_label(self):
#         amount = rolInfo.objects.get(id=1)
#         field_label = rolInfo._meta.get_field('rol_amount').verbose_name
#         self.assertEquals(field_label, 'Cantidad')
#
#     def test_rol_description_label(self):
#         description = rolInfo.objects.get(id=1)
#         field_label = rolInfo._meta.get_field('rol_description').verbose_name
#         self.assertEquals(field_label, 'Descripción del rol')
#
# class testMaxLenght(object):
#         def setUpTestData(cls):
#         # Set up non-modified objects used by all test methods
#         category_cat=category.objects.create(category="emprendimiento")
#         location_loc= location.objects.create(location='Morelos');
#         rol= rolInfo.objects.create(rol_name='Periodista', rol_due_date='10-10-2018', rol_amount='2', rol_description='Tendrá que escribir mucho', rol_location = location_loc)
#
#         pro_pro = project.objects.create(pro_name='Pitch&Catch', pro_description='Es un evento de emprendimiento',
#                pro_video='https://www.youtube.com/watch?v=CcTl_ln4RNw',pro_about_us="Somos estudiantes",
#                 pro_phrase='es sin fines de lucro',pro_creation_date='2018-10-10', pro_category= category_cat,
#                  pro_location=location_loc, pro_roles=rol);
#         img= projectImg.objects.create(pro_img='nombre.txt', pro=pro_pro)
#
#     def test_pro_name_max(self):
#         project_Name = project.objects.get(id=1)
#         max_length = project._meta.get_field('pro_name').max_length
#         self.assertEquals(max_length, 40)
#
#     def test_pro_video_max(self):
#         pro_video = project.objects.get(id=1)
#         max_length = project._meta.get_field('pro_video').max_length
#         self.assertEquals(max_length,200 )
#
#     def test_pro_about_us_max(self):
#         pro_about_us = project.objects.get(id=1)
#         max_length = project._meta.get_field('pro_about_us').max_length
#         self.assertEquals(max_length, 800)
#
#     def test_pro_phrase_max(self):
#         pro_phrase = project.objects.get(id=1)
#         max_length = project._meta.get_field('pro_phrase').verbose_name
#         self.assertEquals(max_length, 200)
#
# class testURL(object):
#         def setUpTestData(cls):
#         # Set up non-modified objects used by all test methods
#         category_cat=category.objects.create(category="emprendimiento")
#         location_loc= location.objects.create(location='Morelos');
#         rol= rolInfo.objects.create(rol_name='Periodista', rol_due_date='10-10-2018', rol_amount='2', rol_description='Tendrá que escribir mucho', rol_location = location_loc)
#
#         pro_pro = project.objects.create(pro_name='Pitch&Catch', pro_description='Es un evento de emprendimiento',
#                pro_video='https://www.youtube.com/watch?v=CcTl_ln4RNw',pro_about_us="Somos estudiantes",
#                 pro_phrase='es sin fines de lucro',pro_creation_date='2018-10-10', pro_category= category_cat,
#                  pro_location=location_loc, pro_roles=rol);
#         img= projectImg.objects.create(pro_img='nombre.txt', pro=pro_pro)
#
#     def test_get_absolute_url(self):
#         project = project.objects.get(id=1)
#         self.assertEquals(project.get_absolute_url(), '/project_app/project/1')
#
#  class testDates(object):
#         # Set up non-modified objects used by all test methods
#         dateInPast = datetime.date.today() - datetime.timedelta(days=1)
#         dateInFuture = datetime.date.today() + datetime.timedelta(weeks=4) + datetime.timedelta(days=1)
#
#         category_cat=category.objects.create(category="emprendimiento")
#         location_loc= location.objects.create(location='Morelos');
#         rol= rolInfo.objects.create(rol_name='Periodista', rol_due_date=dateInFuture, rol_amount='2', rol_description='Tendrá que escribir mucho', rol_location = location_loc)
#
#         form = project.objects.create(pro_name='Pitch&Catch', pro_description='Es un evento de emprendimiento',
#                pro_video='https://www.youtube.com/watch?v=CcTl_ln4RNw',pro_about_us="Somos estudiantes",
#                 pro_phrase='es sin fines de lucro',pro_creation_date=dateInPast, pro_category= category_cat,
#                  pro_location=location_loc, pro_roles=rol);
#         img= projectImg.objects.create(pro_img='nombre.txt', pro=pro_pro)
#
#         def test_date_in_past(self):
#             self.assertTrue(form.is_valid())
#
# class ProjectUpdateView(LoginRequiredMixin, generic.UpdateView):
#     model = ProjectUpdate
#     template_name ='project_app/project.html'
#
#     def get_queryset(self):
#         return ProjectUpdate.objects.filter(person=self.request.user).filter(status__exact='o')
#
#

#TESTS MARTIN
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
        self.project1= project.objects.create(pro_name='sofa',pro_description= '<b>Prueba de diseno </b>',pro_video= 'https://www.youtube.com/watch?v=bdQhytHcZnY',pro_about_us= 'Somos creadores de casa', pro_phrase= 'casa casa',pro_creation_date= '2018-10-10', pro_category=project_category, pro_location=project_location)
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
        self.project1= project.objects.create(pro_name='nosofa',pro_description= '<b>HOLA</b>',pro_video= 'https://www.youtube.com/watch?v=bdQhytHcZnY',pro_about_us= 'Somos creadores de casa', pro_phrase= 'casa casa',pro_creation_date= '2018-10-10', pro_category=project_category, pro_location=project_location)
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
        response=self.client.get(reverse_lazy('project_app:delete', args=[create.id]))
        self.assertEquals(response.status_code, 200)
        #Not redirection, first a confirmation is needed
        response=self.client.post(reverse_lazy('project_app:delete', args=[create.id]))
        print(response.content)
        #Redirect and delete
        self.assertEquals(response.status_code, 302)
        exists = project.objects.filter(pro_name='nosofa').exists()
        self.assertEqual(exists, False)

##NOT AUTHENTICATION
    def test_see_details(self):
    #     #Sin pasar parámetros de content
        create=self.create_project()
        # print(create.id)
        # print(create.pro_name)
        response=self.client.get(reverse_lazy('project_app:project', args=[create.id, slugify(create.pro_name)]))
        # rq = self.client.post(reverse_lazy('project_app:project') , args=[create.id, slugify(create.pro_name)])
        # response=ProjectDetailView.as_view()(request)
        # print (response.content)
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "nosofa")

    def format_description(self):
        create=self.create_project()
        response=self.client.get(reverse_lazy('project_app:project', args=[create.id, slugify(create.pro_name)]))
        self.assertContains(response,"<b>HOLA</b>")

    def test_update_details(self):
        login = self.client.login(username='norco', password='solecito')
        create=self.create_project()
        create.pro_name='Casona'
        self.assertEquals(create.pro_name, 'Casona')

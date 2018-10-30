from django.test import TestCase
import datetime

from project_app.models import project, category, location, rolInfo, projectImg
from django.contrib.auth.models import User;
from project_app.forms import formProject, formProjectAddRol, formImg, rol_formset
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from project_app.forms import CreateProjectForm, formProject
# Create your tests here.
"""
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

"""
""" TESTS DE ANGIE """

class createRol(TestCase): #PASA
    def setUp(self):
        rol_location= location.objects.create(location='Morelos');
        rol= rolInfo.objects.create(rol_name='Periodista', rol_due_date='2018-10-10', rol_amount='2', rol_description='Tendrá que escribir mucho', rol_location = rol_location)
    def test_createRol_exist(self):
        exists = rolInfo.objects.filter(rol_name='Periodista').exists()
        self.assertEqual(exists, True)
"""
class createRol2(TestCase): #PASA
    def setUp(self):
        rol_location= location.objects.create(location='Morelos');
        rol= rolInfo.objects.create(rol_name='Periodistas', rol_due_date='10-10-2018', rol_amount='2', rol_description='Tendrá que escribir mucho2', rol_location = rol_location)
    def test_createRol2_exist(self):
        exists = rolInfo.objects.filter(rol_name='Periodistas').exists()
        self.assertEqual(exists, False)

class uploadImage(TestCase): #PASA
    def setUp(self):
        project_category= category.objects.create(category='Cocina');
        project_location= location.objects.create(location='Queretar0');
        #project_rol= rolInfo.objects.create(rol_name='Periodista', rol_due_date='2018-10-10', rol_amount='2', rol_description='Tendrá que escribir mucho', rol_location=project_location)
        self.project1 = project.objects.create(pro_name='Pitch&Catch', pro_description='Es un evento de emprendimiento', pro_video='https://www.youtube.com/watch?v=CcTl_ln4RNw',pro_about_us="Somos estudiantes", pro_phrase='es sin fines de lucro', pro_creation_date='2018-10-10', pro_category=project_category, pro_location=project_location)
        #self.project1.pro_roles.set(project_rol)
        img= projectImg.objects.create(pro_img='nombre.png', pro=self.project1)
    def test_uploadImage_exist(self):
        exists = projectImg.objects.filter(pro_img='nombre.png').exists()
        self.assertEqual(exists, True)


class uploadImage2(TestCase): #PASA
    def setUp(self):
        project_category=category.objects.create(category="emprendimiento2")
        project_location= location.objects.create(location='Morelos2');
        #rol= rolInfo.objects.create(rol_name='Periodista2', rol_due_date='2018-10-10', rol_amount='2', rol_description='Tendrá que escribir mucho', rol_location = location_loc)

        self.project2 = project.objects.create(pro_name='Pitch&Catch2', pro_description='Es un evento de emprendimiento',pro_video='https://www.youtube.com/watch?v=CcTl_ln4RNw',pro_about_us="Somos estudiantes",pro_phrase='es sin fines de lucro',pro_creation_date='2018-10-10', pro_category= project_category,pro_location=project_location)
        img= projectImg.objects.create(pro_img='hola.jpg', pro=self.project2)
    def test_uploadImage2_exist(self):
        exists = projectImg.objects.filter(pro_img='hola.jpg').exists()
        self.assertEqual(exists, True)

class uploadImage3(TestCase):
    def setUp(self):
        category_cat=category.objects.create(category="cocina")
        location_loc= location.objects.create(location='Baja California');
        #rol= rolInfo.objects.create(rol_name='Periodista', rol_due_date='2018-10-10', rol_amount='2', rol_description='Tendrá que escribir mucho', rol_location = location_loc)

        self.pro_pro = project.objects.create(pro_name='Pitch&Catch', pro_description='Es un evento de emprendimiento',pro_video='https://www.youtube.com/watch?v=CcTl_ln4RNw',pro_about_us="Somos estudiantes",pro_phrase='es sin fines de lucro',pro_creation_date='2018-10-10', pro_category= category_cat,pro_location=location_loc)
        img= projectImg.objects.create(pro_img='nombre.pdf', pro=self.pro_pro)
    def test_uploadImage3_exist(self):
        exists = projectImg.objects.get(pro_img='nombre.pdf')
        print(exists)
        self.assertEqual(exists, False)


class createCategory(TestCase): #PASA
        def setUp(self):
            pro_category= category.objects.create(category='Basketball');
        def test_createCategory_exist(self):
            exists = category.objects.filter(category='Basketball').exists()
            self.assertEqual(exists, True)


class createCategory2(TestCase):
        def setUp(self):
            pro_category= category.objects.create(category=' ');
        def test_createCategory2_exist(self):
            exists = category.objects.filter(category=' ').exists()
            print(category.objects.filter(category=' ').exists())
            self.assertEqual(exists, False)

class testLabels(TestCase):  #PASA
    def setUp(self):
        # Set up non-modified objects used by all test methods
        project_category=category.objects.create(category="emprendimiento2")
        project_location= location.objects.create(location='Morelos2');
        rol= rolInfo.objects.create(rol_name='Periodista2', rol_due_date='2018-10-10', rol_amount='2', rol_description='Tendrá que escribir mucho', rol_location = project_location)
        self.project2 = project.objects.create(pro_name='Pitch&Catch2', pro_description='Es un evento de emprendimiento',pro_video='https://www.youtube.com/watch?v=CcTl_ln4RNw',pro_about_us="Somos estudiantes",pro_phrase='es sin fines de lucro',pro_creation_date='2018-10-10', pro_category= project_category,pro_location=project_location)

        #self.project2 = project.objects.create(pro_name='Pitch&Catch2', pro_description='Es un evento de emprendimiento',pro_video='https://www.youtube.com/watch?v=CcTl_ln4RNw',pro_about_us="Somos estudiantes",pro_phrase='es sin fines de lucro',pro_creation_date='2018-10-10', pro_category= project_category,pro_location=project_location)
        #img= projectImg.objects.create(pro_img='hola.jpg', pro=self.project2)

    def test_category_cat_label(self):  #PASA
        cat = project.objects.get(id=1)
        field_label = cat._meta.get_field('pro_description').verbose_name
        self.assertEquals(field_label,'Descripción')

    def test_rol_name_label(self):      #PASA
        rolname = rolInfo.objects.get(rol_name='Periodista2')
        field_label = rolname._meta.get_field('rol_name').verbose_name
        self.assertEquals(field_label, 'Nombre del puesto')


    def test_location_label(self):      #PASA
        loc = location.objects.get(location='Morelos2')
        field_label = location._meta.get_field('location').verbose_name
        self.assertEquals(field_label, 'Ubicación')

    def test_rol_due_date_label(self):      #PASA
        due_date = rolInfo.objects.get(rol_name='Periodista2')
        field_label = due_date._meta.get_field('rol_due_date').verbose_name
        self.assertEquals(field_label, 'Fecha límite para aplicar')

    def test_rol_amount_label(self):        #PASA
        amount = rolInfo.objects.get(rol_name='Periodista2')
        field_label = amount._meta.get_field('rol_amount').verbose_name
        self.assertEquals(field_label, 'Cantidad de puestos disponibles')

    def test_rol_description_label(self):   #PASA
        description = rolInfo.objects.get(rol_name='Periodista2')
        field_label = description._meta.get_field('rol_description').verbose_name
        self.assertEquals(field_label, 'Descripción del rol')


class testMaxLenght(TestCase):      #PASA
    def setUp(self):
        # Set up non-modified objects used by all test methods
        category_cat=category.objects.create(category="emprendimiento")
        location_loc= location.objects.create(location='Morelos');
        rol= rolInfo.objects.create(rol_name='Periodista', rol_due_date='2018-10-10', rol_amount='2', rol_description='Tendrá que escribir mucho', rol_location = location_loc)

        self.project2 = project.objects.create(pro_name='Pitch&Catch2', pro_description='Es un evento de emprendimiento',pro_video='https://www.youtube.com/watch?v=CcTl_ln4RNw',pro_about_us="Somos estudiantes",pro_phrase='es sin fines de lucro',pro_creation_date='2018-10-10', pro_category= category_cat,pro_location=location_loc)
        img= projectImg.objects.create(pro_img='nombre.txt', pro=self.project2)

    def test_pro_name_max(self):        ##PASA
        #project_Name = project.objects.get(id=1)
        max_length = project._meta.get_field('pro_name').max_length
        self.assertEquals(max_length, 40)

    def test_pro_video_max(self):       #PASA
        #pro_video = project.objects.get(id=1)
        max_length = project._meta.get_field('pro_video').max_length
        self.assertEquals(max_length,200 )

    def test_pro_about_us_max(self):    #PASA
        #pro_about_us = project.objects.get(id=1)
        max_length = project._meta.get_field('pro_about_us').max_length
        self.assertEquals(max_length, 800)

    def test_pro_phrase_max(self):      #PASA
        #pro_phrase = project.objects.get(id=1)
        max_length = project._meta.get_field('pro_phrase').max_length
        self.assertEquals(max_length, 200)


class RenewBookFormTest(TestCase):
    def test_renew_form_date_in_past(self):
        date = datetime.date.today() - datetime.timedelta(days=80) #today munus 80 day
        form_data = {'pro_creation_date': date}
        form = formProject(data=form_data)
        self.assertTrue(form.is_valid())

class createRol(TestCase): #PASA
    #def setUp(self):
        #rol_location= location.objects.create(location='Morelos');
        #rol= rolInfo.objects.create(rol_name='Periodista', rol_due_date='2018-10-10', rol_amount='2', rol_description='Tendrá que escribir mucho', rol_location = rol_location)
    def test_createRol_exist(self):
        try:
            rol_location= location.objects.create(location='Morelos');
            rol= rolInfo.objects.create(rol_name='Periodista', rol_due_date='2018-10-10', rol_amount='-2', rol_description='Tendrá que escribir mucho', rol_location = rol_location)

            #self.assertEqual(len(self.verificationErrors), 0)  # no errors
        except AssertionError as e:
            #for message in self.verificationErrors:
            print(str(message))
            #raise  # < HERE

class createRol(TestCase): #PASA
    def setUp(self):
        project_category=category.objects.create(category="emprendimiento2")
        project_location= location.objects.create(location='Morelos2');
        #rol= rolInfo.objects.create(rol_name='Periodista2', rol_due_date='2018-10-10', rol_amount='2', rol_description='Tendrá que escribir mucho', rol_location = location_loc)

        self.project2 = project.objects.create(pro_name='', pro_description='Es un evento de emprendimiento',pro_video='https://www.youtube.com/watch?v=CcTl_ln4RNw',pro_about_us="Somos estudiantes",pro_phrase='es sin fines de lucro',pro_creation_date='2018-10-10', pro_category= project_category,pro_location=project_location)
        img= projectImg.objects.create(pro_img='hola.jpg', pro=self.project2)
    def test_createRol_exist(self):
        exists = project.objects.get(id=1)
        self.assertEqual(exists, False)

class testURL(TestCase):
    def setUp(self):
        # Set up non-modified objects used by all test methods
        category_cat=category.objects.create(category="emprendimiento")
        location_loc= location.objects.create(location='Morelos');
        rol= rolInfo.objects.create(rol_name='Periodista2', rol_due_date='2018-10-10', rol_amount='2', rol_description='Tendrá que escribir mucho', rol_location = location_loc)
        self.project2 = project.objects.create(pro_name='Pitch', pro_description='Es un evento de emprendimiento',pro_video='https://www.youtube.com/watch?v=CcTl_ln4RNw',pro_about_us="Somos estudiantes",pro_phrase='es sin fines de lucro',pro_creation_date='2018-10-10', pro_category= category_cat,pro_location=location_loc)
        img= projectImg.objects.create(pro_img='nombre.txt', pro=self.project2)

    def test_get_absolute_url(self):
        pro = project.objects.get(id=1)
        print(pro)
        print(pro.get_absolute_url())
        self.assertEquals(pro.get_absolute_url(), '/project_app/project/1/Pitch')

class testDates(TestCase):
    def setUp(self):
        # Set up non-modified objects used by all test methods
        dateInPast = datetime.date.today() - datetime.timedelta(days=1)
        dateInFuture = datetime.date.today() + datetime.timedelta(weeks=4) + datetime.timedelta(days=1)

        category_cat=category.objects.create(category="emprendimiento")
        location_loc= location.objects.create(location='Morelos');
        rol= rolInfo.objects.create(rol_name='Periodista', rol_due_date=dateInFuture, rol_amount='2', rol_description='Tendrá que escribir mucho', rol_location = location_loc)

        form = project.objects.create(pro_name='Pitch&Catch', pro_description='Es un evento de emprendimiento',
               pro_video='https://www.youtube.com/watch?v=CcTl_ln4RNw',pro_about_us="Somos estudiantes",
                pro_phrase='es sin fines de lucro',pro_creation_date=dateInPast, pro_category= category_cat,
                 pro_location=location_loc);
        form.pro_roles.set(pro_roles = rol)
        img= projectImg.objects.create( pro_img = 'nombre.txt', pro = pro_pro )

    def test_date_in_past(self):
            self.assertFalse(form.is_valid())



class testDatesRol(TestCase):
    def setUp(self):
        rol_location= location.objects.create(location='Morelos');
        rol= rolInfo.objects.create(rol_name='Periodistas', rol_due_date='1997-10-10', rol_amount='2', rol_description='Tendrá que escribir mucho2', rol_location = rol_location)
    def test_testDatesRol(self):
        exists = rolInfo.objects.filter(rol_name='Periodistas').exists()
        self.assertEqual(exists, False)

class ProjectUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = project#ProjectUpdate
    template_name ='project_app/project.html'

    def get_queryset(self):
        return ProjectUpdate.objects.filter(person=self.request.user).filter(status__exact='o')
"""

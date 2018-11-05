from django.test import TestCase

from .models import project, category, location, rolInfo
from django.contrib.auth.models import User;
# Create your tests here.

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

    def test_project_no_exist(self):
        exists = project.objects.filter(pro_name='Micasa2').exists()
        self.assertEqual(exists, False)


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

    def test_project_no_exist(self):
        exists = project.objects.filter(pro_name='sofa2').exists()
        self.assertEqual(exists, False)

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

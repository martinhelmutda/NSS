from django.test import TestCase, RequestFactory

from project_app.models import category, subcategory, state, city, rolInfo, project, project_rol, user_project, status
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.template.defaultfilters import slugify
from django.test import Client

# Create your tests here.
class SearchTests(TestCase):
    def setUp(self):
        self.user1= User.objects.create_user('user1', None, 'tes1234')
        #Category
        self.category1=category.objects.create(category="Musica")
        self.subcategory1=subcategory.objects.create(subcategory="Salsa", category=self.category1)

        self.category2=category.objects.create(category="Videojuego")
        self.subcategory2=subcategory.objects.create(subcategory="Accion", category=self.category2)
        #Location
        self.state1=state.objects.create(state="Morelos")
        self.city1=city.objects.create(city="Cuernavaca", state=self.state1)

        self.state2=state.objects.create(state="Queretaro")
        self.city2=city.objects.create(city="Queretaro", state=self.state2)
        #Rol
        self.rol1=rolInfo.objects.create(rol_name="Profesor", rol_due_date="2018-12-12", rol_amount=1, rol_description="Profesor de salsa", rol_city=self.city1, rol_state=self.state1)
        #project
        self.project3 = project.objects.create(pro_name="proyecto otro", pro_description="Es otro chido", pro_video="https://www.youtube.com/watch?v=G1FIfaP7Tu0",pro_about_us="LDAW students", pro_phrase="No", pro_creation_date="2017-01-10", pro_group=True, pro_category= self.category2, pro_subcategory= self.subcategory2, pro_city=self.city2, pro_state=self.state2, pro_user=self.user1)
        self.project2 = project.objects.create(pro_name="proyecto LDAW", pro_description="Es un buen chido", pro_video="https://www.youtube.com/watch?v=G1FIfaP7Tu0",pro_about_us="LDAW students", pro_phrase="No", pro_creation_date="2017-01-10", pro_group=False, pro_category= self.category1, pro_subcategory= self.subcategory1, pro_city=self.city1, pro_state=self.state1, pro_user=self.user1)
        self.project1 = project.objects.create(pro_name="proyecto chido", pro_description="Es un buen projecto", pro_video="https://www.youtube.com/watch?v=G1FIfaP7Tu0",pro_about_us="we are students", pro_phrase="No", pro_creation_date="2017-01-10", pro_group=False, pro_category= self.category1, pro_subcategory= self.subcategory1, pro_city=self.city1, pro_state=self.state1, pro_user=self.user1)
        self.project1_rol= project_rol.objects.create(pro=self.project1, rol=self.rol1)

    def test_search_name(self):
        response = self.client.get('/search/?q=proyecto LDAW')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'proyecto LDAW')
        self.assertNotContains(response, 'proyecto chido')

    def test_search_category(self):
        response = self.client.get('/search/?id_pro_category=Musica&id_pro_subcategory=&q=')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'proyecto LDAW')
        self.assertContains(response, 'proyecto chido')
        self.assertNotContains(response, 'proyecto otro')

    def test_search_state(self):
        response = self.client.get('/search/?id_pro_state=Morelos&id_pro_city=&q=')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'proyecto LDAW')
        self.assertContains(response, 'proyecto LDAW')
        self.assertNotContains(response, 'proyecto otro')

    def test_search_subcategory(self):
        response = self.client.get('/search/?id_pro_category=Musica&id_pro_subcategory=Salsa&q=')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'proyecto LDAW')
        self.assertContains(response, 'proyecto chido')
        self.assertNotContains(response, 'proyecto otro')

    def test_search_city(self):
        response = self.client.get('/search/?id_pro_state=Morelos&id_pro_city=Cuernavaca&q=')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'proyecto LDAW')
        self.assertContains(response, 'proyecto LDAW')
        self.assertNotContains(response, 'proyecto otro')

    def test_various_fields(self):
        response = self.client.get('/search/?id_pro_category=Musica&id_pro_subcategory=Salsa&id_pro_state=Morelos&id_pro_city=Cuernavaca&q=proyecto LDAW')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'proyecto LDAW')
        self.assertContains(response, 'proyecto LDAW')
        self.assertNotContains(response, 'proyecto otro')

    def test_search_group(self):
        response = self.client.get('/search/?id_pro_group=on&q=')
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'proyecto LDAW')
        self.assertNotContains(response, 'proyecto LDAW')
        self.assertContains(response, 'proyecto otro')

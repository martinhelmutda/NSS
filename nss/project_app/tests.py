from django.test import TestCase, RequestFactory

from project_app.models import category, subcategory, state, city, rolInfo, project, project_rol, user_project, status
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.template.defaultfilters import slugify
from django.test import Client
from django.test import TestCase, RequestFactory
from project_app.models import category, subcategory, state, city, rolInfo, project, project_rol, user_project, status
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.template.defaultfilters import slugify
from django.test import Client
from django.core.files.uploadedfile import SimpleUploadedFile
from account_app.forms import *
from django.core.validators import FileExtensionValidator
from django.core.validators import validate_image_file_extension
from account_app.models import Profile
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy

""" TESTS DE ANGIE """
class SearchTests(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_superuser(username='testuser1', email="example2@example.com",
                                                  password='pass1')
        self.useraux = UserProfileInfo.objects.create(user = self.user1, profile_pic = SimpleUploadedFile(name='k.png', content=open('media/profile_pics/k.png', 'rb').read(), content_type='image/png'), portfolio_site = "Google.com")
        self.user1.save()
        self.useraux.save()

        #Category
        self.category1=category.objects.create(category="Musica")
        self.subcategory1=subcategory.objects.create(subcategory="Salsa", category=self.category1)

        self.category2=category.objects.create(category="Videojuego")
        self.subcategory2=subcategory.objects.create(subcategory="Accion", category=self.category2)
        #Location
        self.state1=state.objects.create(state="Morelos")
        self.city1=city.objects.create(city="Cuernavaca", state=self.state1)
        self.city3=city.objects.create(city="Xochitepec", state=self.state1)

        self.state2=state.objects.create(state="Queretaro")
        self.city2=city.objects.create(city="Queretaro", state=self.state2)
        #Rol
        self.rol1=rolInfo.objects.create(rol_name="Profesor", rol_due_date="2018-12-12", rol_amount=1, rol_description="Profesor de salsa", rol_city=self.city1, rol_state=self.state1)
        #project
        self.project3 = project.objects.create(pro_name="proyecto otro", pro_description="Es otro chido", pro_video="https://www.youtube.com/watch?v=G1FIfaP7Tu0",pro_about_us="LDAW students", pro_phrase="No", pro_creation_date="2017-01-10", pro_group=True, pro_category= self.category2, pro_subcategory= self.subcategory2, pro_city=self.city2, pro_state=self.state2, pro_user=self.user1)
        self.project2 = project.objects.create(pro_name="proyecto LDAW", pro_description="Es un buen chido", pro_video="https://www.youtube.com/watch?v=G1FIfaP7Tu0",pro_about_us="LDAW students", pro_phrase="No", pro_creation_date="2017-01-10", pro_group=False, pro_category= self.category1, pro_subcategory= self.subcategory1, pro_city=self.city1, pro_state=self.state1, pro_user=self.user1)
        self.project1 = project.objects.create(pro_name="proyecto chido", pro_description="Es un buen projecto", pro_video="https://www.youtube.com/watch?v=G1FIfaP7Tu0",pro_about_us="we are students", pro_phrase="No", pro_creation_date="2017-01-10", pro_group=False, pro_category= self.category1, pro_subcategory= self.subcategory1, pro_city=self.city1, pro_state=self.state1, pro_user=self.user1)
        self.project1_rol= project_rol.objects.create(pro=self.project1, rol=self.rol1)
    def test_see_aplications(self):
        print("........................TEST test_see_aplications")
        response = self.client.get('/profiles_app/?q=testuser4')
        self.assertEqual(response.status_code, 200)
        print('Codigo exitoso', response.status_code)
        print(response)
        self.assertContains(response, 'testuser')
        self.assertNotContains(response, 'testuser12')
    def test_publish_group(self):
        print("........................TEST test_publish_group")
        self.group1 = project.objects.create(pro_name="grupo chido", pro_description="Es un buen projecto", pro_video="https://www.youtube.com/watch?v=G1FIfaP7Tu0",pro_about_us="we are students", pro_phrase="No, no cobramos admision", pro_creation_date="2017-01-10", pro_group=True, pro_category= self.category1, pro_subcategory= self.subcategory1, pro_city=self.city1, pro_state=self.state1, pro_user=self.user1)
        exists= project.objects.filter(id = self.group1.id)
        print(self.group1.id)
        self.assertEqual(len(exists),0)
    def test_dependent_dropdown_city(self):
        def get_dependent_dropdown_info(self, dd1):
            print(dd1)
            res=[]
            citys = city.objects.filter(state=dd1)
            for x in citys:
                res.append(str(x))
            return res
        print("........................TEST test_dependent_dropdown")
        print(get_dependent_dropdown_info(self,self.state1))
        self.assertEqual(get_dependent_dropdown_info(self,self.state1),['Cuernavaca', 'Xochitepec'])
    def test_dependent_dropdown_subactegory(self):
        def get_dependent_dropdown_info(self, dd1):
            print(dd1)
            res=[]
            subcategorys = subcategory.objects.filter(category=dd1)
            for x in subcategorys:
                res.append(str(x))
            return res
        print("........................TEST test_dependent_dropdown_subactegory")
        print(get_dependent_dropdown_info(self,self.category1))
        self.assertEqual(get_dependent_dropdown_info(self,self.category1),['Salsa'])

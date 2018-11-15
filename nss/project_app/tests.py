from django.test import TestCase, RequestFactory

from project_app.models import category, subcategory, state, city, rolInfo, project, project_rol, user_project, status
from django.contrib.auth.models import User;
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.template.defaultfilters import slugify

""" TESTS DE ANGIE """
class TestCase(TestCase):
    def setUp(self):
        self.user1= User.objects.create_user('user1', None, 'tes1234')
        #Category
        self.category1=category.objects.create(category="Musica")
        self.subcategory1=subcategory.objects.create(subcategory="Salsa", category=self.category1)
        #Location
        self.state1=state.objects.create(state="Morelos")
        self.city1=city.objects.create(city="Cuernavaca", state=self.state1)
        #Rol
        self.rol1=rolInfo.objects.create(rol_name="Profesor", rol_due_date="2018-12-12", rol_amount=1, rol_description="Profesor de salsa", rol_city=self.city1, rol_state=self.state1)
        #project
        self.project1 = project.objects.create(pro_name="proyecto chido", pro_description="Es un buen projecto", pro_video="https://www.youtube.com/watch?v=G1FIfaP7Tu0",pro_about_us="we are students", pro_phrase="No", pro_creation_date="2017-01-10", pro_group=True, pro_category= self.category1, pro_subcategory= self.subcategory1, pro_city=self.city1, pro_state=self.state1, pro_user=self.user1)
        self.project1_rol= project_rol.objects.create(pro=self.project1, rol=self.rol1)
        #status
        self.status1=status.objects.create(status="enviada", status_text="Cancelar aplicacion")#ENVIADA
        self.status2=status.objects.create(status="cancelada", status_text="Aplicar")#CANCELADA
    def test_apply_one_rol(self): #I want to apply for the role that fits me the most
        application1 = user_project.objects.create(up_project=self.project1, up_user = self.user1, up_rolInfo=self.rol1, up_status=self.status1)
        exists_application1 = user_project.objects.filter(up_project=self.project1, up_user = self.user1, up_rolInfo=self.rol1, up_status=self.status1)
        print("........................TEST test_apply_one_rol")
        print("({}): {}".format(application1.up_rolInfo, application1.up_project))
        self.assertEqual(len(exists_application1),1)
    def test_apply_multiple_roles(self): #I want to apply for severa projects and roles at once
        self.rol2 = rolInfo.objects.create(rol_name="Fotografo", rol_due_date="2019-10-10", rol_amount=2, rol_description="Creador de contenido digital", rol_city=self.city1, rol_state=self.state1)
        application1 = user_project.objects.create(up_project=self.project1, up_user = self.user1, up_rolInfo=self.rol1, up_status=self.status1)
        application2 = user_project.objects.create(up_project=self.project1, up_user = self.user1, up_rolInfo=self.rol2, up_status=self.status1)
        exists_application1 = user_project.objects.filter(up_project=self.project1, up_user = self.user1, up_status=self.status1)
        print("........................TEST test_apply_multiple_roles")
        for application in exists_application1.all():
            print("({}): {}".format(application.up_rolInfo, application.up_project))
        self.assertEqual(len(exists_application1),2)
    def test_cancel_application(self): #I want to cancel my application
        application3 = user_project.objects.create(up_project=self.project1, up_user = self.user1, up_rolInfo=self.rol1, up_status=self.status1)
        print("........................TEST test_cancel_application")
        print(application3.up_rolInfo,'-> ',application3.up_status)
        application3.up_status=self.status2
        print(application3.up_rolInfo,'-> ',application3.up_status)
        self.assertEqual(application3.up_status,self.status2)
    def test_post_multiple_rols(self): #I want to post all the positions that I am looking for, for my project.
        self.project2 = project.objects.create(pro_name="proyecto LDAW", pro_description="Es un buen chido", pro_video="https://www.youtube.com/watch?v=G1FIfaP7Tu0",pro_about_us="LDAW students", pro_phrase="No", pro_creation_date="2017-01-10", pro_group=True, pro_category= self.category1, pro_subcategory= self.subcategory1, pro_city=self.city1, pro_state=self.state1, pro_user=self.user1)
        #Rol
        self.rols1 = rolInfo.objects.create(rol_name="Profesor", rol_due_date="2018-12-12", rol_amount=1, rol_description="Profesor de salsa", rol_city=self.city1, rol_state=self.state1)
        self.rols2 = rolInfo.objects.create(rol_name="Fotografo", rol_due_date="2019-10-10", rol_amount=2, rol_description="Creador de contenido digital", rol_city=self.city1, rol_state=self.state1)
        self.rols3 = rolInfo.objects.create(rol_name="Ingeniero en sonido", rol_due_date="2019-11-09", rol_amount=1, rol_description="ALguien que el dia de la presentacion nos ayude con un equipo de sonido", rol_city=self.city1, rol_state=self.state1)
        #Add to many to many
        self.project1_rol= project_rol.objects.create(pro=self.project2, rol=self.rols1)
        self.project2_rol= project_rol.objects.create(pro=self.project2, rol=self.rols2)
        self.project3_rol= project_rol.objects.create(pro=self.project2, rol=self.rols3)
        exists = project_rol.objects.filter(pro=self.project2)
        print("........................TEST test_post_multiple_rols")
        for x in exists:
            print("({}): {}".format(x.rol, x.pro))
        self.assertEqual(len(exists),3)

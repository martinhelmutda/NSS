cd nssfrom django.test import TestCase, RequestFactory

from project_app.models import category, subcategory, state, city, rolInfo, project, project_rol, user_project, status
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.template.defaultfilters import slugify
from django.test import Client

""" TESTS DE ANGIE """
class TestCase(TestCase):
    def setUp(self):
        self.client = Client()
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
        self.project2 = project.objects.create(pro_name="proyecto LDAW", pro_description="Es un buen chido", pro_video="https://www.youtube.com/watch?v=G1FIfaP7Tu0",pro_about_us="LDAW students", pro_phrase="No", pro_creation_date="2017-01-10", pro_group=False, pro_category= self.category1, pro_subcategory= self.subcategory1, pro_city=self.city1, pro_state=self.state1, pro_user=self.user1)
        self.project1 = project.objects.create(pro_name="proyecto chido", pro_description="Es un buen projecto", pro_video="https://www.youtube.com/watch?v=G1FIfaP7Tu0",pro_about_us="we are students", pro_phrase="No", pro_creation_date="2017-01-10", pro_group=False, pro_category= self.category1, pro_subcategory= self.subcategory1, pro_city=self.city1, pro_state=self.state1, pro_user=self.user1)
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
        self.assertEqual(application3.up_status, self.status2)

    def test_post_multiple_rols(self): #I want to post all the positions that I am looking for, for my project.
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
        """
    def test_decide_rol_name(self): #I want to add my own name of role (different from dropdown)
        self.rol3 = rolInfo.objects.create(rol_name="Otro", rol_name_other="", rol_due_date="2019-11-09", rol_amount=1, rol_description="Este rol no tiene nombre", rol_city=self.city1, rol_state=self.state1)
        self.project2 = project.objects.create(pro_name="proyecto LDAW", pro_description="Es un buen chido", pro_video="https://www.youtube.com/watch?v=G1FIfaP7Tu0",pro_about_us="LDAW students", pro_phrase="No", pro_creation_date="2017-01-10", pro_group=True, pro_category= self.category1, pro_subcategory= self.subcategory1, pro_city=self.city1, pro_state=self.state1, pro_user=self.user1)
        self.project4_rol= project_rol.objects.create(pro=self.project2, rol=self.rol3)
        exists = rolInfo.objects.filter(rol_description="Este rol no tiene nombre")
        print("..........TEST test_decide_rol_name")
        self.assertEqual(len(exists),0)

    def test_see_admission_charges(self): # I want to know if the group charges admission
        group = project.objects.create(pro_name="Grupo de ajederez", pro_description="Es un club chido", pro_video="https://www.youtube.com/watch?v=G1FIfaP7Tu0",pro_about_us="Somos amateurs con ganas de comptir con gente nueva", pro_phrase="Es completamente gratuito", pro_creation_date="2017-01-10", pro_group=True, pro_category= self.category1, pro_subcategory= self.subcategory1, pro_city=self.city1, pro_state=self.state1, pro_user=self.user1)
        project4_rol= project_rol.objects.create(pro=group, rol=self.rol3)
        exists = rolInfo.objects.filter(rol_description="Este rol no tiene nombre")
        print("........................TEST test_see_admission_charges")
        self.assertEqual(len(exists),0)
    def test_see_projects(self): #I want to be able to see the projects I created
        loginresponse = self.client.login(username='user',password='passphrase')
        response=self.client.post(reverse('project_app:projects'))
        print("........................TEST test_see_projects")
        self.assertEqual(response.status_code, 200)
    def test_add_url(self): # I want to be able to add a link to a video
        self.project_new_new = project.objects.create(pro_name="proyecto h", pro_description="Es un buen chido", pro_video="tch?v=_zPlr-o-YEQ&list=RD_zPlr-o-YEQ&start_radio=1", pro_about_us="LDAW students", pro_phrase="No", pro_creation_date="2017-01-10", pro_group=False, pro_category= self.category1, pro_subcategory= self.subcategory1, pro_city=self.city1, pro_state=self.state1, pro_user=self.user1)
        print("........................TEST test_add_url")
        exists = project.objects.filter(pro_video="tch?v=_zPlr-o-YEQ&list=RD_zPlr-o-YEQ&start_radio=1")
        self.assertEqual(len(exists),0) #son dos por el self del setUp
        """
    def test_diferent_location(self): #I want to add a location for each role and one for the proyect
        state2=state.objects.create(state="Querétaro")
        city2=city.objects.create(city="Celaya", state=state2)
        project_new = project.objects.create(pro_name="proyecto LDAW", pro_description="Es un buen chido", pro_video="https://www.youtube.com/watch?v=G1FIfaP7Tu0",pro_about_us="LDAW students", pro_phrase="No", pro_creation_date="2017-01-10", pro_group=False, pro_category= self.category1, pro_subcategory= self.subcategory1, pro_city=self.city1, pro_state=self.state1, pro_user=self.user1)
        rols_new = rolInfo.objects.create(rol_name="Profesor", rol_due_date="2018-12-12", rol_amount=1, rol_description="Profesor de salsa", rol_city=city2, rol_state=state2)
        project_rol_new= project_rol.objects.create(pro=project_new, rol=rols_new)
        temp = project_rol.objects.get(pro=project_new, rol=rols_new)
        print("........................TEST test_diferent_location")
        print("({}): {}".format(temp.pro.pro_state, temp.pro.pro_city))
        print("({}): {}".format(temp.rol.rol_state, temp.rol.rol_city))
        self.assertNotEqual(temp.pro.pro_state,temp.rol.rol_state)
        self.assertNotEqual(temp.pro.pro_city,temp.rol.rol_city)
    def test_see_project_info(self): #I want to be able to see the projects I created
        state2=state.objects.create(state="Querétaro")
        city2=city.objects.create(city="Celaya", state=state2)
        project_new = project.objects.create(pro_name="proyecto LDAW", pro_description="Es un buen chido", pro_video="https://www.youtube.com/watch?v=G1FIfaP7Tu0",pro_about_us="LDAW students", pro_phrase="No", pro_creation_date="2017-01-10", pro_group=False, pro_category= self.category1, pro_subcategory= self.subcategory1, pro_city=self.city1, pro_state=self.state1, pro_user=self.user1)
        print("........................TEST test_see_project_info")
        print(project_new.pro_name)
        print("({}): {}".format('descripcion', project_new.pro_description))
        print("({}): {}".format('about us', project_new.pro_about_us))
        print("({}): {}".format('date', project_new.pro_creation_date))
        self.assertEqual(len(project.objects.all()), 3) #son tres por el self del setUp
    def test_apply_multiple_projects(self): #I want to be able to see projects even when I'm already in one
        self.user2= User.objects.create_user('user2', None, 'tes1234')
        application1 = user_project.objects.create(up_project=self.project1, up_user = self.user2, up_rolInfo=self.rol1, up_status=self.status1)
        application2 = user_project.objects.create(up_project=self.project2, up_user = self.user2, up_rolInfo=self.rol1, up_status=self.status1)
        exists= user_project.objects.filter(up_user = self.user2, up_status=self.status1)
        print("........................TEST test_apply_multiple_projects")
        for x in exists:
            print("({}): {}".format(x.up_project, x.up_rolInfo))

        self.assertEqual(len(exists), 2)

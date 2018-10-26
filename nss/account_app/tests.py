#Last modified by César Buenfil on Oct 19,2018
from django.test import TestCase
from account_app.models import category, location, rol, rolInfo, project
# Create your tests here.


class category(TestCase):
    def setUp(self):
        category.objects.create(category='Deportes')

    def test_area(self):
        new_category = category.objects.get(category='Deportes')
        self.assertEqual(str(new_category), 'Deportes')

class project(TestCase):
    def set_up(self):
        proyecto.objects.create(
            pro_name = "Proyecto Chido!",
            pro_description = "Es un proyecto chido & padre",
            pro_video = "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            pro_about_us = "Somos un grupo chido",
            pro_phrase = "Lo chido está en nosotros",
            pro_creation_date = date.today()
        )

    def correct_input(self):
        proyecto1 = proyecto.objects.get(pro_name="Proyecto Chido!")
        print(proyecto1)
        #self.assertTrue(form.is_valid())
        #self.assertEqual(lion.speak(), 'The lion says "roar"')

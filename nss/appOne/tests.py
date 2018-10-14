from django.test import TestCase
from appOne.models import area, location, rol, rolInfo, proyecto
# Create your tests here.


class area(TestCase):
    def setUp(self):
        area.objects.create(area='Deportes')

    def test_area(self):
        nuevaArea = area.objects.get(area='Deportes')
        self.assertEqual(str(nuevaArea), 'Deportes')

class proyecto(TestCase):
    def setUp(self):
        proyecto.objects.create(
            ProName="Proyecto Chido!",
            ProDescription="Es un proyecto chido & padre",
            ProVideo="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            ProAboutUs="Somos un grupo chido",
            ProFrase="Lo chido está en nosotros",
            ProCreationDate=date.today()
        )

    def correctInput(self):
        proyecto1 = proyecto.objects.get(ProName="Proyecto Chido!")
        print(proyecto1)
        #self.assertTrue(form.is_valid())
        #self.assertEqual(lion.speak(), 'The lion says "roar"')

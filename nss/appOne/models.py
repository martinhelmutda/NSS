from django.db import models

# Create your models here.

class area(models.Model):
     area = models.CharField(max_length = 50, unique = True)

     def __str__(self):
        return self.area

class proyecto(models.Model):
    nombre_proyecto = models.CharField(max_length = 50, unique = True)

    def __str__(self):
        return self.nombre_proyecto

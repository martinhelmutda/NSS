from django.db import models

# Create your models here.

class area(models.Model):
     area = models.CharField(primary_key=True,max_length = 50, unique = True, default='')

     def __str__(self):
        return self.area

class location(models.Model):
     location = models.CharField(primary_key=True,max_length = 50, unique = True, default='')

     def __str__(self):
        return self.location

class rol(models.Model):
    rol = models.CharField(primary_key=True, max_length = 15, unique = True, default='')

    def __str__(self):
        return self.rol


class rolInfo(models.Model):
    rol =  models.ForeignKey(rol, on_delete=models.CASCADE)
    fechaLimite=models.DateField()
    rolcantidad= models.PositiveIntegerField(default=1)
    rolDescripcion = models.TextField(max_length=800, default='')
    rolLocation=models.ForeignKey('location', on_delete=models.PROTECT,default='')

    def __str__(self):
        return self.rolDescripcion

class proyecto(models.Model):
    #Info del proyecto
    proName = models.CharField(max_length=40,default='')
    proDescription = models.TextField(max_length=800,default='')
    proVideo =models.URLField()
    proAboutUs= models.TextField(max_length=800, default='')
    proFrase= models.CharField(max_length=200, default='')
    proCreationDate = models.DateField()
    proArea=models.ForeignKey('area', on_delete=models.PROTECT,default='')
    proLocation=models.ForeignKey('location', on_delete=models.PROTECT,default='')
    proRoles = models.ManyToManyField('rolInfo') # https://stackoverflow.com/questions/2216974/django-modelform-for-many-to-many-fields

    def __str__(self):
        return self.proName

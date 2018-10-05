from django.db import models

# Create your models here.

class area(models.Model):
     area = models.CharField(max_length = 50, unique = True, default='Sin area')

     def __str__(self):
        return self.area

class location(models.Model):
     location = models.CharField(max_length = 50, unique = True, default='Sin ubicacion')

     def __str__(self):
        return self.location

class rol(models.Model):
    rol = models.CharField(primary_key=True, max_length = 15, unique = True, default='')

    def __str__(self):
        return self.rol


class rolInfo(models.Model):
    rol =  models.ForeignKey(rol, on_delete=models.CASCADE)
    fechaLimite=models.DateField()
    cantidad= models.PositiveIntegerField(default=1)
    rolDescripcion = models.TextField(max_length=800, default='')
    RolLocation=models.ForeignKey('location', on_delete=models.PROTECT,default='')

    def __str__(self):
        return self.rolDescripcion

class proyecto(models.Model):
    #Info del proyecto
    #id=models.CharField( unique = True, max_length=40, primary_key=True)
    ProName = models.CharField( max_length=40,default='')
    ProDescription = models.TextField(max_length=800,default='')
    ProVideo =models.URLField()
    ProAboutUs= models.TextField(max_length=800, default='')
    ProFrase= models.CharField(max_length=200, default='')
    ProCreationDate = models.DateField()
    ProArea=models.ForeignKey('area', on_delete=models.PROTECT,default='')
    proLocation=models.ForeignKey('location', on_delete=models.PROTECT,default='')
    proRoles = models.ManyToManyField('rolInfo')

    def __str__(self):
        return self.ProName

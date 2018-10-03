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

class proyecto(models.Model):
    #Info del proyecto
    ProName = models.CharField(unique = True, max_length=40)
    ProDescription = models.CharField(max_length=40)
    ProVideo =models.URLField()
    ProAboutUs= models.CharField(max_length=40, default='')
    ProFrase= models.CharField(max_length=40, default='')
    ProCreationDate = models.DateField()
    ProArea=models.ForeignKey('area', on_delete=models.PROTECT)
    proLocation=models.ForeignKey('location', on_delete=models.PROTECT)

    def __str__(self):
        return self.ProName

#Last modified by César Buenfil on Oct 19,2018
from django.db import models
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    #additional
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username

class category(models.Model):
     category = models.CharField(primary_key=True,max_length = 50, unique = True, default='')

     def __str__(self):
        return self.category

class location(models.Model):
     location = models.CharField(primary_key=True,max_length = 50, unique = True, default='')

     def __str__(self):
        return self.location

class rol(models.Model):
    rol = models.CharField(primary_key=True, max_length = 15, unique = True, default='')

    def __str__(self):
        return self.rol

class rolInfo(models.Model):
    rol_name =  models.ForeignKey(rol, on_delete=models.CASCADE)
    rol_due_date = models.DateField()
    rol_amount = models.PositiveIntegerField(default=1)
    rol_description = models.TextField(max_length=800, default='')
    rol_location = models.ForeignKey('location', on_delete=models.PROTECT,default='')

    def __str__(self):
        return self.rol_description

class project(models.Model):
    #Info del proyecto
    pro_name = models.CharField(max_length=50,default='')
    pro_description = models.TextField(max_length=800,default='')
    pro_video = EmbedVideoField() # models.URLField()
    pro_about_us = models.TextField(max_length=800, default='')
    pro_phrase = models.TextField(max_length=700, default='')
    pro_creation_date = models.DateField()
    pro_category = models.ForeignKey('category', on_delete=models.PROTECT,default='')
    pro_location = models.ForeignKey('location', on_delete=models.PROTECT,default='')
    pro_roles = models.ManyToManyField('rolInfo') # https://stackoverflow.com/questions/2216974/django-modelform-for-many-to-many-fields

    def __str__(self):
        return self.pro_name

class projectImg(models.Model):
    pro_img = models.ImageField(default='', upload_to='pro_img', blank=True)
    pro = models.ForeignKey('project', on_delete=models.CASCADE,default='')

    def __str__(self):
        return str(self.pro_img)

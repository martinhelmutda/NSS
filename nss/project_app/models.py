"""
Last modified: ANgélica Güemes
date: November 8
Time: 8:40
"""
from django.db import models
from embed_video.fields import EmbedVideoField
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


#class Page(models.Model):
#    title = models.CharField(verbose_name="Título", max_length=200)
#    content = RichTextField(verbose_name="Contenido")
#    order = models.SmallIntegerField(verbose_name="Orden", default=0)
#    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
#    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
#
#    class Meta:
#        verbose_name = "página"
#        verbose_name_plural = "páginas"
#        ordering = ['order', 'title']
#
#    def __str__(self):
#        return self.title

class category(models.Model):
     category = models.CharField(primary_key=True,max_length = 50, unique = True, default='')

     def __str__(self):
        return self.category

class subcategory(models.Model):
     subcategory = models.CharField(primary_key=True,max_length = 50, unique = True, default='')
     category = models.ForeignKey('category', on_delete=models.PROTECT,default='')

     def __str__(self):
        return self.subcategory

class state(models.Model): #estado
     state = models.CharField(primary_key=True,max_length = 50, unique = True, default='')

     def __str__(self):
        return self.state

class city(models.Model): #ciudad
     city = models.CharField(primary_key=True,max_length = 50, unique = True, default='')
     state = models.ForeignKey('state', on_delete=models.PROTECT,default='')
     def __str__(self):
        return self.city

class rolInfo(models.Model):#info del rol
    rol_name =  models.CharField(max_length = 150,  default='')
    rol_name_other=models.CharField(max_length = 150,  default='', blank=True)
    rol_due_date = models.DateField()
    rol_amount = models.PositiveIntegerField(default=1)
    rol_description = models.TextField(max_length=800, default='')
    rol_city = models.ForeignKey('city', on_delete=models.PROTECT,default='')
    rol_state = models.ForeignKey('state', on_delete=models.PROTECT,default='')


    def __str__(self):
        return self.rol_name

class project(models.Model):
    #Info del proyecto
    pro_name = models.CharField(max_length=40,default='')
    #Import RichTextField
    pro_description = RichTextField(verbose_name="Descripción", max_length=5000)
    pro_video = EmbedVideoField() # models.URLField()
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    pro_about_us = models.TextField(max_length=800, default='')
    pro_phrase = models.CharField(max_length=200, default='')
    pro_creation_date = models.DateField()
    pro_img = models.ImageField(default='', upload_to='pro_img', blank=True)# null=true se pone null en la base de datos como entrada
    pro_group = models.BooleanField()
    pro_likes = models.PositiveIntegerField(default=0)
    pro_save_times = models.PositiveIntegerField(default=0)

    pro_category = models.ForeignKey('category', on_delete=models.PROTECT,default='')
    pro_subcategory = models.ForeignKey('subcategory', on_delete=models.PROTECT,default='')

    pro_city = models.ForeignKey('city', on_delete=models.PROTECT,default='')
    pro_state = models.ForeignKey('state', on_delete=models.PROTECT,default='')

    pro_roles = models.ManyToManyField('rolInfo', through='project_rol') # https://stackoverflow.com/questions/2216974/django-modelform-for-many-to-many-fields

    pro_user = models.ForeignKey(User, on_delete=models.CASCADE, default="", blank=True, null=True)

    class Meta:
            verbose_name = "project_app"
            verbose_name_plural = "project_app"
            ordering = ['order','pro_name']

    def __str__(self):
        return self.pro_name

class projectImg(models.Model):#Ya no se usa
    pro_img = models.ImageField(default='', upload_to='pro_img', blank=True)
    pro = models.ForeignKey('project', on_delete=models.CASCADE,default='')

    def __str__(self):
        return str(self.pro_img)

class project_rol(models.Model):#Tabla NN
    id= models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    pro = models.ForeignKey('project', related_name='project', on_delete=models.CASCADE,default='')
    rol= models.ForeignKey('rolInfo', related_name='rolInfo', on_delete=models.CASCADE,default='')
    def __str__(self):
        return str(self.rol)

class user_project(models.Model):
    up_project = models.ForeignKey('project', related_name='up_project', on_delete=models.CASCADE,default='')
    up_user = models.ForeignKey(User, on_delete=models.CASCADE, default="", blank=True, null=True)
    up_rolInfo =  models.ForeignKey('rolInfo', related_name='up_rolInfo', on_delete=models.CASCADE,default='')
    up_status = models.ForeignKey('status', related_name='upstatus', on_delete=models.CASCADE,default='')
    
    def __str__(self):
        return str(self.up_project)

class status(models.Model):
    status= models.CharField(primary_key=True,max_length = 50, unique = True, default='')
    status_text= models.CharField(max_length=40,default='')
    def __str__(self):
        return self.status

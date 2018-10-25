from django.db import models
from embed_video.fields import EmbedVideoField
from ckeditor.fields import RichTextField

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


class Project(models.Model):
    #Info del proyecto
    pro_name = models.CharField(max_length=40,default='')

    #Import RichTextField
    pro_description = RichTextField(verbose_name="Descripción")
    # pro_video = EmbedVideoField() # models.URLField()
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    pro_about_us = models.TextField(max_length=800, default='')
    pro_phrase = models.CharField(max_length=200, default='')
    pro_creation_date = models.DateField()
    # pro_category = models.ForeignKey('category', on_delete=models.PROTECT,default='')
    pro_location = models.ForeignKey('location', on_delete=models.PROTECT,default='')
    pro_roles = models.ManyToManyField('rolInfo') # https://stackoverflow.com/questions/2216974/django-modelform-for-many-to-many-fields

    class Meta:
            verbose_name = "project_app"
            verbose_name_plural = "project_app"
            ordering = ['order','pro_name']

    def __str__(self):
        return self.pro_name

from django.db import models
from django.core.validators import FileExtensionValidator
from embed_video.fields import EmbedVideoField
from ckeditor.fields import RichTextField
from .validators import validate_file_extension, validate_past_date

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
     category = models.CharField(primary_key=True,max_length = 50, unique = True, blank=False)

     def __str__(self):
        return self.category

class location(models.Model):
     location = models.CharField(primary_key=True,max_length = 50, unique = True, default='', verbose_name='Ubicación')

     def __str__(self):
        return self.location

class rolInfo(models.Model):
    rol_name =  models.CharField(max_length = 150, verbose_name="Nombre del puesto") ###Checar que no metan vacio
    rol_due_date = models.DateField(verbose_name='Fecha límite para aplicar', validators=[validate_past_date])
    rol_amount = models.PositiveIntegerField(default=1,verbose_name="Cantidad de puestos disponibles")
    rol_description = models.TextField(max_length=800, default='', verbose_name='Descripción del rol')
    rol_location = models.ForeignKey('location', on_delete=models.PROTECT,default='')

    def __str__(self):
        return self.rol_description

class project(models.Model):
    #Info del proyecto
    pro_name = models.CharField(max_length=40,default='', verbose_name="Nombre del proyecto")

    #Import RichTextField
    pro_description = RichTextField(verbose_name="Descripción")
    pro_video = EmbedVideoField(verbose_name="Video") # models.URLField()
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    pro_about_us = models.TextField(max_length=800, default='', verbose_name="Acerca de nosotros")
    pro_phrase = models.CharField(max_length=200, default='', verbose_name="Indica si el proyecto tiene fines de lucro")
    pro_creation_date = models.DateField()
    pro_category = models.ForeignKey('category', on_delete=models.PROTECT,default='')
    pro_location = models.ForeignKey('location', on_delete=models.PROTECT,default='')
    pro_roles = models.ManyToManyField('rolInfo') # https://stackoverflow.com/questions/2216974/django-modelform-for-many-to-many-fields

    class Meta:
        verbose_name = "project_app"
        verbose_name_plural = "project_app"
        ordering = ['order','pro_name']

    def __str__(self):
        return self.pro_name

class projectImg(models.Model):
    pro_img = models.ImageField(upload_to='pro_img', validators=[FileExtensionValidator(['png','jpg'])])
    pro = models.ForeignKey('project', on_delete=models.CASCADE,default='')

    def __str__(self):
        return str(self.pro_img)

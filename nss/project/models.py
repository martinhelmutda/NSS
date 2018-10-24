from django.db import models
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

class Project(models.Model):
    #Info del proyecto
    pro_name = models.CharField(max_length=40,default='')
    pro_description = models.TextField(max_length=800,default='')
    pro_video = EmbedVideoField() # models.URLField()
    pro_about_us = models.TextField(max_length=800, default='')
    pro_phrase = models.CharField(max_length=200, default='')
    pro_creation_date = models.DateField()
    pro_category = models.ForeignKey('category', on_delete=models.PROTECT,default='')
    pro_location = models.ForeignKey('location', on_delete=models.PROTECT,default='')
    pro_roles = models.ManyToManyField('rolInfo') # https://stackoverflow.com/questions/2216974/django-modelform-for-many-to-many-fields
    
    def __str__(self):
        return self.pro_name

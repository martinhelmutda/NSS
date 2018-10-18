#Last modified by César Buenfil on Oct 14,2018

from django import forms
from django.forms import formset_factory, CharField, ModelMultipleChoiceField, ModelChoiceField, BaseFormSet
from django.db import models
from django.core import validators
from app_one.models import category, project, location, rolInfo, rol
#from crispy_forms.helper import FormHelper

class formProject(forms.Form):
    #Info del project
    pro_name = forms.CharField(label='Nombre',max_length=40, widget=forms.TextInput(attrs={ 'class': 'field'}))
    pro_description = forms.CharField(label='Descripción',widget=forms.Textarea, required=False)
    pro_video = forms.URLField(label='Link a video', widget=forms.TextInput(attrs={'placeholder':'https://www.youtube.com/watch?v=dQw4w9WgXcQ'}),required=False)
    pro_about_us = forms.CharField(label='Acerca de nosotros', widget=forms.Textarea, required=False)
    pro_phrase = forms.CharField(label='Frase')
    pro_creation_date = forms.DateField(label='Inició',widget=forms.DateInput(attrs={'class':'datepicker'}), required=False)
    pro_category = ModelChoiceField(label='Categoría',widget=forms.Select(attrs={'class': 'ui fluid dropdown'}) ,queryset=category.objects.all(), initial=0)
    pro_location = ModelChoiceField(label='Ubicación',widget=forms.Select(attrs={'class': 'ui fluid dropdown'}) ,queryset=location.objects.all(), initial=0)
    pro_img = forms.ImageField(label='Imagen')
    #Integrantes

    #ProConfirmation = forms.BooleanField(label='Recibir correo de confirmación',required=False)
    #email = forms.EmailField()
    #verify_email = forms.EmailField(label='Enter your email again:')
    def clean(self):
        cleaned_data = super().clean()
        #name=all_clean_data['ProName']

class formProjectAddRol(forms.Form):
    rol_name = ModelChoiceField(label='rol',widget=forms.Select(attrs={'class': 'ui fluid dropdown'}) ,queryset=rol.objects.all(), initial=0)
    rol_due_date =  forms.DateField(label='Fecha límite para aplicar',widget=forms.DateInput(attrs={'class':'datepicker'}))
    rol_amount = forms.IntegerField(label='Cantidad', widget=forms.TextInput(attrs={'class':'field'}))
    rol_description = forms.CharField(label='Descripción del rol',widget=forms.Textarea)
    rol_location = ModelChoiceField(label='Ubicación del rol',queryset=location.objects.all(), widget=forms.Select(attrs={'class':'ui fluid dropdown'}), initial=0)
    #def clean(self):
    #    cleaned_data = super().clean()

class baseProjectAddRol(BaseFormSet):
    #rolNombre = []
    #rolFechaLimite = []
    #rolCantidad = []
    #rolDescripcion = []
    #rolNomrolLocationbre = []
    #info=[]
    def clean(self):
        info=[]
        for form in self.forms:
            #Nombre=form.cleaned_data['rolNombre']
            #rolNombre.append(Nombre)
            #FechaLimite=form.cleaned_data['rolFechaLimite']
            #rolFechaLimite.append(FechaLimite)
            #Cantidad+=form.cleaned_data['rolCantidad']
            #rolCantidad.append(Cantidad)
            #Descripcion+=form.cleaned_data['rolDescripcion']
            #rolDescripcion.append(Descripcion)
            #Location+=form.cleaned_data['rolLocation']
            #rolLocation.append(Location)
            cleaned_data = super().clean()
            info.append(cleaned_data)



rol_formset = formset_factory(formProjectAddRol, extra=2)#, formset=baseprojectAddRol, max_num=10)
#https://medium.com/@taranjeet/adding-forms-dynamically-to-a-django-formset-375f1090c2b0
#https://stackoverflow.com/questions/501719/dynamically-adding-a-form-to-a-django-formset-with-ajax
"""
Set required fields on forms
Set widgets
Validar fechas
Check selection on display. To add category or rol -> https://www.caktusgroup.com/blog/2018/05/07/creating-dynamic-forms-django/
Add table Integrantes

class Formproject(forms.Form):
    #Info del project
    ProName = forms.CharField(label='Nombre', max_length=40)
    ProDescription = forms.CharField(label='Descripción',widget=forms.Textarea)
    ProVideo =forms.URLField(label='Link a video')
    ProAboutUs= forms.CharField(label='Acerca de nosotros', widget=forms.Textarea, required=False)
    ProLocation = forms.CharField(label='Ubicación')
    ProFrase= forms.CharField(label='Frase')
    ProCreationDate = forms.DateField(label='Inició',widget=forms.SelectDateWidget())
    Procategory = forms.CharField( label='Área', widget=forms.Select(choices=categoryS_CHOICES))
    #Integrantes
    #Roles
    RolNombre=forms.CharField( label='Rol', widget=forms.Select(choices=ROL_CHOICES))
    ProConfirmation = forms.BooleanField(label='Recibir correo de confirmación',required=False)
    RolExpirationDate = forms.DateField(label='Fecha límite para aplicar',widget=forms.SelectDateWidget())

    #email = forms.EmailField()
    #verify_email = forms.EmailField(label='Enter your email again:')


    def clean(self):
        all_clean_data = super().clean()
        #email = all_clean_data['email']
        #vmail = all_clean_data['verify_email']

        #if email != vmail:
            #raise forms.ValidationError("MAKE SURE EMAILS MATCH!")
"""

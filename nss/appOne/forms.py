from django import forms
from django.forms import formset_factory, CharField, ModelMultipleChoiceField, ModelChoiceField, BaseFormSet
from django.db import models
from django.core import validators
from appOne.models import area, proyecto, location, rolInfo, rol
from crispy_forms.helper import FormHelper

class formProyecto(forms.Form):
    #Info del proyecto
    proName = forms.CharField(label='Nombre',max_length=40, widget=forms.TextInput(attrs={'placeholder': 'Ejemplo: Kunigo Web Site', 'class': 'field'}))
    proDescription = forms.CharField(label='Descripción',widget=forms.Textarea)
    proVideo =forms.URLField(label='Link a video', widget=forms.TextInput(attrs={'placeholder':'Ejemplo: www.youtube.com/MyVideo'}))
    proAboutUs= forms.CharField(label='Acerca de nosotros', widget=forms.Textarea, required=False)
    proFrase= forms.CharField(label='Frase')
    proCreationDate = forms.DateField(label='Inició',widget=forms.SelectDateWidget(attrs={'class':'ui fluid dropdown'}), required=False)
    proLocation = ModelChoiceField(label='Ubicación',widget=forms.Select(attrs={'class': 'ui fluid dropdown'}) ,queryset=location.objects.all())
    #ProImagen = forms.ImageField(label='Imagen',required=False)
    #ProImagen = forms.ImageField(label='Imagen',required=False)
    #Integrantes

    #ProConfirmation = forms.BooleanField(label='Recibir correo de confirmación',required=False)
    #email = forms.EmailField()
    #verify_email = forms.EmailField(label='Enter your email again:')
    def clean(self):
        cleaned_data = super().clean()
        #name=all_clean_data['ProName']

class formProyectoAddRol(forms.Form):
    rolNombre=ModelChoiceField(label='Rol', queryset=rol.objects.all(), widget=forms.TextInput(attrs={'class':'field'}))
    rolFechaLimite =  forms.DateField(label='Fecha límite para aplicar',widget=forms.SelectDateWidget(attrs={'class':'ui fluid dropdown'}))
    rolCantidad = forms.IntegerField(label='Cantidad', widget=forms.TextInput(attrs={'placeholder':'1', 'class':'field'}))
    rolDescripcion=forms.CharField(label='Descripción del rol',widget=forms.Textarea)
    rolLocation = ModelChoiceField(label='Ubicación del rol',queryset=location.objects.all(), widget=forms.Select(attrs={'class':'ui fluid dropdown'}))
    #def clean(self):
    #    cleaned_data = super().clean()

class baseProyectoAddRol(BaseFormSet):
    rolNombre = []
    rolFechaLimite = []
    rolCantidad = []
    rolDescripcion = []
    rolNomrolLocationbre = []
    def clean(self):
        for form in self.forms:
            Nombre=form.cleaned_data['rolNombre']
            rolNombre.append(Nombre)
            FechaLimite=form.cleaned_data['rolFechaLimite']
            rolFechaLimite.append(FechaLimite)
            Cantidad+=form.cleaned_data['rolCantidad']
            rolCantidad.append(Cantidad)
            Descripcion+=form.cleaned_data['rolDescripcion']
            rolDescripcion.append(Descripcion)
            Location+=form.cleaned_data['rolLocation']
            rolLocation.append(Location)


rolesFormset = formset_factory(formProyectoAddRol, formset=baseProyectoAddRol, max_num=10)
#https://medium.com/@taranjeet/adding-forms-dynamically-to-a-django-formset-375f1090c2b0
#https://stackoverflow.com/questions/501719/dynamically-adding-a-form-to-a-django-formset-with-ajax
"""
Set required fields on forms
Set widgets
Validar fechas
Check selection on display. To add area or rol -> https://www.caktusgroup.com/blog/2018/05/07/creating-dynamic-forms-django/
Add table Integrantes

class FormProyecto(forms.Form):
    #Info del proyecto
    ProName = forms.CharField(label='Nombre', max_length=40)
    ProDescription = forms.CharField(label='Descripción',widget=forms.Textarea)
    ProVideo =forms.URLField(label='Link a video')
    ProAboutUs= forms.CharField(label='Acerca de nosotros', widget=forms.Textarea, required=False)
    ProLocation = forms.CharField(label='Ubicación')
    ProFrase= forms.CharField(label='Frase')
    ProCreationDate = forms.DateField(label='Inició',widget=forms.SelectDateWidget())
    ProArea = forms.CharField( label='Área', widget=forms.Select(choices=AREAS_CHOICES))
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

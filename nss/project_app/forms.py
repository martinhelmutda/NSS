from django import forms
from .models import project
from project_app.models import category, project, location, rolInfo,  projectImg
from django.forms import formset_factory, CharField, ModelMultipleChoiceField, ModelChoiceField, BaseFormSet
from django.db import models

ROL_CHOICES= [
    ('---', '---'),
    ('Traductor', 'Traductor'),
    ('Programador', 'Programador'),
    ('Editor_video', 'Editor de video'),
    ('Tesorero', 'Tesorero'),
    ('Otro', 'Otro'),
    ]

class CreateProjectForm(forms.ModelForm):
    class Meta:
        model = project
        exclude = ['pro_roles', "order"]
        widgets = {
            'pro_name' : forms.TextInput(attrs={ 'class': 'field'}),
            'pro_description' : forms.Textarea(),
            'pro_video' : forms.TextInput(attrs={'placeholder':'https://www.youtube.com/watch?v=dQw4w9WgXcQ'}),
            'pro_about_us' : forms.Textarea(),
            'pro_phrase' : forms.Textarea(),
            'pro_creation_date' : forms.DateInput(attrs={'class':'datepicker'}),
            'pro_category' :forms.Select(attrs={'class': 'ui fluid dropdown'}),
            'pro_location' : forms.Select(attrs={'class': 'ui fluid dropdown'}),
            'pro_img' : forms.ImageField(label='Imagen'),
        }
        labels = {
            'pro_name': "Nombre de proyecto",
            'pro_description': "Escribe una descripción general de tu proyecto",
            'pro_video': "Añade algun link a un video relacionado con tu proyecto",
            'pro_about_us': "¿Quiénes son? Añade una descripción sobre los creadores del proyecto",
            'pro_phrase': "Indica si el proyetco tiene fines de lucro",
            'pro_creation_date': "Inicio del proyecto",
            'pro_location': "Ubicación del proyecto",
            'pro_category' :"Indica en qué categoria clasifica",
            'pro_img': "Agrega las imagenes que quieras compartir sobre tu proyecto",
        }
        help_texts = { #Sale justo abajo del field
            #'pro_name': 'Escribe el nombre del proyecto',
            'pro_description': "Nota: Debe ser un link a un video en youtube.",
            'pro_creation_date': "Nota: Indica cuanto cuando se comenzó a planear este proyecto",
            'pro_img': "Nota: Firmato png y jpg",
        }
        error_messages = {
            'pro_name': {
                'max_length':'Este nombre es demasiado grande',
            },
        }

class CreateRolForm(forms.ModelForm):
    class Meta:
        model = rolInfo
        fields = ['rol_name', 'rol_due_date', 'rol_amount', 'rol_description', 'rol_location']
        widgets = {
            'rol_name' : forms.TextInput(attrs={ 'class': 'field'}),
            'rol_description' :forms.Textarea(),
            'rol_due_date' : forms.DateInput(attrs={'class':'datepicker'}),
            'rol_amount' : forms.TextInput(),
            'rol_location' :  forms.Select(attrs={'class': 'ui fluid dropdown'}),
            #'pro_img' : forms.ImageField(label='Imagen'),
        }
        labels = {
            'rol_name' : "Nombre del puesto",
            'rol_due_date' : "Fecha límite para aplicar",
            'rol_amount' : "¿Cuántos puestos como estos necesitas?",
            'rol_description':"Descripcion del puesto",
            'rol_location' :  "Ubicación del rol",
            #'pro_creation_date': "Inicio del proyecto",
            #'pro_location': "Ubicación del proyecto",
            #'pro_category' :"Indica en qué categoria clasifica",
            #'pro_img': "Agrega las imagenes que quieras compartir sobre tu proyecto",
        }
        help_texts = { #Sale justo abajo del field
            #'pro_name': 'Escribe el nombre del proyecto',
            #'pro_description': "Nota: Debe ser un link a un video en youtube.",
            #'pro_creation_date': "Nota: Indica cuanto cuando se comenzó a planear este proyecto",
            #'pro_img': "Nota: Firmato png y jpg",
        }
        error_messages = {
            #'pro_name': {
            #    'max_length':'Este nombre es demasiado grande',
            #},
        }

class formProject(forms.Form):
    #Info del project
    pro_description = forms.CharField(label='Descripción',widget=forms.Textarea, required=False)
    pro_name = forms.CharField(label='Nombre',max_length=40, widget=forms.TextInput(attrs={ 'class': 'field'}))
    pro_video = forms.URLField(label='Link a video', widget=forms.TextInput(attrs={'placeholder':'https://www.youtube.com/watch?v=dQw4w9WgXcQ'}),required=False)
    pro_about_us = forms.CharField(label='Acerca de nosotros', widget=forms.Textarea, required=False)
    pro_phrase = forms.CharField(label='Indica si el proyecto implica recompensa monetaria', widget=forms.Textarea)
    pro_creation_date = forms.DateField(label='Inició',widget=forms.DateInput(attrs={'class':'datepickerProyect'}), required=False)
    pro_category = ModelChoiceField(label='Categoría',widget=forms.Select(attrs={'class': 'ui fluid dropdown'}) ,queryset=category.objects.all(), initial=0)
    pro_location = ModelChoiceField(label='Ubicación',widget=forms.Select(attrs={'class': 'ui fluid dropdown'}) ,queryset=location.objects.all(), initial=0)
    #Integrantes

    #ProConfirmation = forms.BooleanField(label='Recibir correo de confirmación',required=False)
    #email = forms.EmailField()
    #verify_email = forms.EmailField(label='Enter your email again:')
    def clean(self):
        cleaned_data = super().clean()
        #name=all_clean_data['ProName']

class formProjectAddRol(forms.Form):
    #rol_alternative_name = ModelChoiceField(label='rol',widget=forms.Select(attrs={'class': 'ui fluid dropdown'}) ,queryset=rol.objects.all(), initial=0)
    rol_dropdown_name= forms.CharField(label='Nombre del puesto disponible', widget=forms.Select(attrs={'class': 'ui fluid dropdown'}, choices=ROL_CHOICES))
    rol_alternative_name = forms.CharField(required=False,max_length=40, widget=forms.TextInput(attrs={ 'class': 'field', 'id': 'rol_alternative_name', 'hidden':True,'placeholder':'Indica el nombre del puesto'}))
    rol_due_date =  forms.DateField(label='Fecha límite para aplicar',widget=forms.DateInput(attrs={'class':'datepicker'}), required=False)
    rol_amount = forms.IntegerField(label='Cantidad', widget=forms.TextInput(attrs={'class':'field'}))
    rol_description = forms.CharField(label='Descripción del rol',widget=forms.Textarea)
    rol_location = ModelChoiceField(label='Ubicación del rol',queryset=location.objects.all(), widget=forms.Select(attrs={'class':'ui fluid dropdown'}), initial=0)
    #def clean(self):
    #    cleaned_data = super().clean()

class formImg(forms.ModelForm):
    """docstring forformImg."""
    class Meta():
        model = projectImg
        fields=('pro_img',)


class baseProjectAddRol(BaseFormSet):
    def clean(self):
        return [form.cleaned_data for form in self.forms]

rol_formset = formset_factory(formProjectAddRol, extra=1)#, formset=baseprojectAddRol, max_num=10)

#https://medium.com/@taranjeet/adding-forms-dynamically-to-a-django-formset-375f1090c2b0
#https://stackoverflow.com/questions/501719/dynamically-adding-a-form-to-a-django-formset-with-ajax

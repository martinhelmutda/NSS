"""
Last modified: ANgélica Güemes
date: November 8
Time: 8:40
"""
from django import forms
from .models import project
from project_app.models import category,subcategory, project, city, state, rolInfo,  projectImg
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
        exclude = ['pro_roles', "order", 'pro_likes', 'pro_save_times', 'pro_user']
        widgets = {
            'pro_group': forms.HiddenInput(attrs={'value':False}),
            'pro_name' : forms.TextInput(attrs={ 'placeholder':'Nombre'}),
            'pro_description' : forms.TextInput(),
            'pro_video' : forms.TextInput(attrs={'placeholder':'Link de Youtube'}),
            'pro_about_us' : forms.Textarea(),
            'pro_phrase' : forms.Textarea(),
            'pro_creation_date' : forms.DateInput(attrs={'class':'datepicker'}),
            'pro_category' :forms.Select(attrs={'class': 'ui fluid dropdown', 'placeholder':'Categoría'}),
            'pro_subcategory' :forms.Select(attrs={'class': 'ui fluid dropdown'}),
            'pro_city' : forms.Select(attrs={'class': 'ui fluid dropdown'}),
            'pro_state' : forms.Select(attrs={'class': 'ui fluid dropdown'}),
        }
        labels = {
            'pro_name': "Nombre del proyecto",
            'pro_description': "Escribe una descripción general de tu proyecto",
            'pro_video': "Añade algun link a un video relacionado con tu proyecto",
            'pro_about_us': "¿Quiénes son? Añade una descripción sobre los creadores del proyecto",
            'pro_phrase': "Indica si el proyetco tiene fines de lucro",
            'pro_creation_date': "Inicio del proyecto",
            'pro_category' :"Indica en qué categoria clasifica",
            'pro_city': "Municipio",
            'pro_state' :"Estado",
            'pro_img': "Agrega algun logo o imagen de tu proyecto",
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if project.pro_user is None:
            profile.pro_user =  User.objects.get(user=self.request.user)
            print(profile.pro_user)

        self.fields['pro_city'].queryset = city.objects.none()
        self.fields['pro_subcategory'].queryset = subcategory.objects.none()
        if 'pro_state' in self.data:
            try:
                country_id = self.data.get('pro_state')
                self.fields['pro_city'].queryset = city.objects.filter(state=country_id)#.order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryse
        elif self.instance.pk:
            self.fields['pro_city'].queryset = self.instance.country.city_set#.order_by('name')
        if 'pro_category' in self.data:
            try:
                category_id = self.data.get('pro_category')
                self.fields['pro_subcategory'].queryset = subcategory.objects.filter(category=category_id)#.order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryse
        elif self.instance.pk:
            self.fields['pro_subcategory'].queryset = self.instance.category.subcategory_set#.order_by('name')


class CreateGroupForm(forms.ModelForm):
    class Meta:
        model = project
        exclude = ['pro_roles', "order",  'pro_likes', 'pro_save_times']
        widgets = {
            'pro_group': forms.HiddenInput(attrs={'value':True}),
            'pro_name' : forms.TextInput(attrs={ 'class': 'field'}),
            'pro_description' : forms.TextInput(),
            'pro_video' : forms.TextInput(attrs={'placeholder':'Link de Youtube'}),
            'pro_about_us' : forms.Textarea(),
            'pro_phrase' : forms.Textarea(),
            #'pro_group' : forms.BooleanField(),
            'pro_creation_date' : forms.DateInput(attrs={'class':'datepicker'}),
            'pro_category' :forms.Select(attrs={'class': 'ui fluid dropdown'}),
            'pro_subcategory' :forms.Select(attrs={'class': 'ui fluid dropdown'}),
            'pro_city' : forms.Select(attrs={'class': 'ui fluid dropdown'}),
            'pro_state' : forms.Select(attrs={'class': 'ui fluid dropdown'}),
        }
        labels = {
            'pro_name': "Nombre del grupo",
            'pro_description': "Escribe una descripción general este grupo",
            'pro_video': "Añade algun link a un video relacionado",
            'pro_about_us': "¿Quiénes son? Añade una descripción sobre los creadores del grupo",
            'pro_phrase': "Indica si existe algun tipo de cuota",
            'pro_creation_date': "Inicio del grupo",
            'pro_category' :"Indica en qué categoria clasifica",
            'pro_subcategory' : "¿En qué área encaja tu proyecto?",
            'pro_city': "Municipio",
            'pro_state' :"Estado",
            'pro_img': "Agrega algun logo o imagen del grupo",
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['pro_city'].queryset = city.objects.filter(state=self.data.get('pro_state'))
        # self.fields['pro_city'].queryset = city.objects.none()
        # self.fields['pro_subcategory'].queryset = subcategory.objects.none()
        if 'pro_state' in self.data:
            try:
                country_id = self.data.get('pro_state')
                self.fields['pro_city'].queryset = city.objects.filter(state=country_id)#.order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryse
        elif self.instance.pk:
            self.fields['pro_city'].queryset = self.instance.country.city_set#.order_by('name')
        if 'pro_category' in self.data:
            try:
                category_id = self.data.get('pro_category')
                self.fields['pro_subcategory'].queryset = subcategory.objects.filter(category=category_id)#.order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryse
        elif self.instance.pk:
            self.fields['pro_subcategory'].queryset = self.instance.category.subcategory_set#.order_by('name')

    def clean(self):
        super().clean()
        print(self.cleaned_data['pro_video'])
        #a=self.cleaned_data['pro_video']
        #if not a.contains('youtube') :
        #    print("ENTRA")
        #    msg="Debe ser un video en youtube para que se pueda desplegar en tu proyecto"
        #    self.add_error('pro_video', msg)

class CreateRolForm(forms.ModelForm):

    class Meta:
        model = rolInfo
        fields = ['rol_name', 'rol_name_other','rol_due_date', 'rol_amount', 'rol_description', 'rol_city', 'rol_state']
        widgets = {
            'rol_name' :forms.Select(attrs={'class': 'ui fluid dropdown'}, choices=ROL_CHOICES),
            'rol_name_other' : forms.TextInput( attrs={'placeholder': 'Indique el nombre', 'required':False}),
            'rol_description' :forms.Textarea(),
            'rol_due_date' : forms.DateInput(attrs={'class':'datepicker'}),
            'rol_amount' : forms.TextInput(),
            'rol_city' :  forms.Select(attrs={'class': 'ui fluid dropdown'}),
            'rol_state' :  forms.Select(attrs={'class': 'ui fluid dropdown'}),
        }
        labels = {
            'rol_name' : "Nombre del puesto",
            'rol_name_other' : "",
            'rol_due_date' : "Fecha límite para aplicar",
            'rol_amount' : "¿Cuántos puestos como estos necesitas?",
            'rol_description':"Descripcion del puesto",
            'rol_city' :  "Municipio",
            'rol_state' :  "Estado",
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
            'pro_name': {
                'invalid':'El número debe ser mayor a 0',
            },
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['pro_city'].queryset = city.objects.filter(state=self.data.get('pro_state'))
        self.fields['rol_city'].queryset = city.objects.none()
        if 'rol_state' in self.data:
            print("Hay state")
            try:
                country_id = self.data.get('rol_state')
                self.fields['rol_city'].queryset = city.objects.filter(state=country_id)#.order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryse
        elif self.instance.pk:
            print("No hhuay state")
            self.fields['rol_city'].queryset = self.instance.country.city_set#.order_by('name')

    def clean(self):
        super().clean()
        print(self.cleaned_data['rol_name'])
        print(self.cleaned_data['rol_name_other'])
        if self.cleaned_data['rol_name'] == 'Otro' and self.cleaned_data['rol_name_other'] =='':
            print("ENTRA")
            msg="Tienes que indicar otro nombre"
            self.add_error('rol_name', msg)


#https://medium.com/@taranjeet/adding-forms-dynamically-to-a-django-formset-375f1090c2b0
#https://stackoverflow.com/questions/501719/dynamically-adding-a-form-to-a-django-formset-with-ajax

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
        fields = ['pro_name','pro_description','pro_video', 'pro_about_us', 'pro_phrase', 'pro_creation_date', 'pro_category', 'pro_location', 'pro_roles']
        widgets = {
            'pro_name' : forms.TextInput(attrs={ 'class': 'field'}),
            'pro_description' : forms.Textarea(),
            'pro_video' : forms.TextInput(attrs={'placeholder':'https://www.youtube.com/watch?v=dQw4w9WgXcQ'}),
            'pro_about_us' : forms.Textarea(),
            'pro_phrase' : forms.Textarea(),
            'pro_creation_date' : forms.DateInput(attrs={'class':'datepicker'}),
            'pro_category' :forms.Select( attrs={'class': 'ui fluid dropdown'}),
            'pro_location' : forms.Select(attrs={'class': 'ui fluid dropdown'}),
            'pro_img' : forms.ImageField(label='Imagen'),
        }
        labels = {
            "pro_category": "Categoría",
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
    def clean(self):
        cleaned_data = super().clean()
        rol_alt_name = cleaned_data.get("rol_alternative_name")
        #cc_myself = cleaned_data.get("cc_myself")
        if rol_alt_name=='':
            msg='Debe indicar la categoría'
            self.add_error('cc_myself', msg)


class formImg(forms.ModelForm):
    """docstring forformImg."""

    class Meta():
        model = projectImg
        fields=('pro_img',)
    def clean(self):
        pro_img = self.cleaned_data.get("pro_img", False)
        filetype = magic.from_buffer(pro_img.read())
        if not '.png' in filetype or not '.jpg' in filetype:
            raise ValidationError('No tiene extension valida')
            return pro_img


class baseProjectAddRol(BaseFormSet):
    def clean(self):
        return [form.cleaned_data for form in self.forms]

rol_formset = formset_factory(formProjectAddRol, extra=1)#, formset=baseprojectAddRol, max_num=10)

#https://medium.com/@taranjeet/adding-forms-dynamically-to-a-django-formset-375f1090c2b0
#https://stackoverflow.com/questions/501719/dynamically-adding-a-form-to-a-django-formset-with-ajax

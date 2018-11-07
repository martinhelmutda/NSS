#Last modified by César Buenfil on Oct 19,2018

from django import forms
from django.forms import formset_factory, CharField, ModelMultipleChoiceField, ModelChoiceField, BaseFormSet
from django.db import models
from django.core import validators
from django.contrib.auth.models import User
from account_app.models import UserProfileInfo
from django.conf import settings
from django.core.validators import FileExtensionValidator
from .models import Profile
#from crispy_forms.helper import FormHelper

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    verify_password = forms.CharField(widget=forms.PasswordInput(),label='Enter your password again')
    botcatcher = forms.CharField(required=False,widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    class Meta():
        model = User
        fields = ('username','first_name','last_name','email','password')

    def clean(self):
        all_clean_data = super().clean()
        password = all_clean_data['password']
        verify_password = all_clean_data['verify_password']

        if password != verify_password:
            raise forms.ValidationError("Passwords must match")

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')



        def clean(self):
            all_clean_data = super().clean()



class createProfileForm(forms.Form):
    name = forms.CharField( label='Nombre',required=True)
    email  = forms.EmailField( label='Email', required=True, widget=forms.EmailInput(attrs={'placeholder':'Introduce tu email de contacto'}))
    edad = forms.IntegerField(label='Edad', required=True)
    carreer = forms.CharField( label='Carrera de estudio', required=True)
    ocupation = forms.CharField(label='Ocupación Actual', max_length=100, required=True)
    cv = forms.CharField(label='Trabajos Anteriores', required=True, widget=forms.Textarea())
    experience = forms.CharField(label='Experiencia', max_length=1000, required=True, widget=forms.Textarea())

class ProfileForm(forms.ModelForm):
    """docstring forProfileForm."""
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class':'container'}),
            'bio': forms.Textarea(attrs={'class':'field'}),
            'link': forms.URLInput(attrs={'class':'field'}),
        }


# class CustomImageWidget(forms.ClearableFileInput):
#     input_type = 'image'
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

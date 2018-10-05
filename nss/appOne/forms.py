from django import forms
from django.db import models
from django.core import validators
from appOne.models import area, proyecto, location, rolInfo

class DateInput(forms.DateInput):
    input_type = 'date'


class NewProjectForm(forms.ModelForm):
    class Meta():
         model = proyecto
        # fields = '__all__'
         exclude = ['proRoles']
         labels = {
         'ProName': ('Nombre'),
         'ProDescription': ('Descripción'),
         'ProVideo': ('Video'),
         'ProAboutUs': ('Acerca de nosotros'),
         'ProFrase': ('Frase'),
         'ProCreationDate': ('Fecha de creación'),
         'ProArea': ('Área'),
         'proLocation': ('Ubicación'),
         }
         widgets = {
         'ProCreationDate': DateInput()

         }

class NewRolForm(forms.ModelForm):
    class Meta():
         model = rolInfo
         fields = '__all__'
        # exclude = ['proRoles']
         labels = {
         'rol': ('Rol'),
         'fechaLimite': ('Fecha límite para aplicar'),
         'cantidad': ('Cantidad'),
         'rolDescripcion': ('Descripción'),
         'RolLocation': ('Ubicación'),
         }
         widgets = {
         'fechaLimite': DateInput()

         }



"""
Set required fields on forms
Set widgets
Check selection on display. To add area or rol -> https://www.caktusgroup.com/blog/2018/05/07/creating-dynamic-forms-django/
Add table Rol
Add table integrantes

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

from django import forms
from .models import Project

class CreateProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['pro_name','pro_description','pro_video', 'pro_about_us', 'pro_phrase', 'pro_creation_date', 'pro_category', 'pro_location', 'pro_roles']
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

#Last modified by César Buenfil on Oct 19,2018
from django.db import models
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.validators import FileExtensionValidator
from ckeditor.fields import RichTextField

# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    #additional
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True, validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])])

    def __str__(self):
        return self.user.username

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profiles', null=True, blank=True, validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])])
    bio = RichTextField(verbose_name="biografía", default="My Bio")
    link = models.URLField(max_length=200, null=True, blank=True)


@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    #If there is something that says tha is created, then is not executed. Its false by default
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
        #print("Se acaba de crear un usuario y su perfil enlazado")

#Last modified by César Buenfil on Oct 19,2018
from django.db import models
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    #additional
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True, validators=[FileExtensionValidator(['jpg', 'png'])])

    def __str__(self):
        return self.user.username

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profiles', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)

### Last modified by César Buenfil on Oct 14,2018

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from . import forms
from account_app.forms import  UserForm, UserProfileInfoForm, createProfileForm, ProfileForm
from django.urls import reverse, reverse_lazy
from urllib.parse import urlencode
from project_app.models import project, projectImg, project, rolInfo, city,state, category, subcategory
from project_app import models
from django.db.models import Q
from functools import reduce
from django.views import generic
from braces.views import SelectRelatedMixin
import operator

from django.utils.decorators import method_decorator
#login
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

#Class Based views
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView, UpdateView,
                                DeleteView)
from .models import Profile

# Create your views here.
class IndexView(SelectRelatedMixin, generic.ListView):
    template_name = 'account_app/index.html'
    context_object_name = 'projects'
    model = models.project
    select_related = ("pro_category", "pro_subcategory", "pro_city", "pro_state")

def proper_pagination(posts, index):
    start_index = 0
    end_index = 7
    if posts.number > index:
        start_index = posts.number - index
        end_index = start_index + end_index
    return (start_index, end_index)

@login_required
def special(request):
    return HttpResponse("You are logged in")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True

        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'account_app/registration.html',{'user_form':user_form,
                                                       'profile_form':profile_form,
                                                       'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Account not Active")

        else:
            print("Someone tried to login and failed")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("Invalid login details supplied")

    else:
        return render(request,'account_app/login.html',{})

###Class Based Views

@method_decorator(login_required, name='dispatch')
class ProfileAccountUpdate(UpdateView):
    form_class=ProfileForm
    success_url = reverse_lazy('account_app:profile')
    template_name='account_app/profile_form.html'
    def get_object(self):
        profile_obj, create = Profile.objects.get_or_create(user=self.request.user)
        return profile_obj



"""
    def form_project(request):
        form = forms.formProject()
        if request.method == 'POST':
            form = forms.formProject(request.POST)
            if form.is_valid():
                # DO SOMETHING CODE
                print("VALIDATION SUCCESS!")
                #print("NAME: "+form.cleaned_data['name'])
                #recipients=[]
                #if ProConfirmation:
                    #print("Enviar email!")
                #    send_mail('subject', 'message', 'A01421467@itesm.mx', 'angieguemes@gmail.com')
                #    return HttpResponseRedirect('/thanks/')
        return render(request,'app_one/createPro.html',{'form':form})
"""

from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from account_app.models import Profile
# Create your views here.
class ProfileList(ListView):
    model = Profile
    template_name = 'profiles_app/profile_list.html'

class ProfileDetail(DetailView):
    model = Profile
    template_name = 'profiles_app/profile_detail.html'

    def get_object(self):
        return get_object_or_404(Profile, user__username=self.kwargs['username'])

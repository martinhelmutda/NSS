from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from account_app.models import Profile
from django.db.models import Q
from functools import reduce
from django.views import generic
from braces.views import SelectRelatedMixin
import operator
# Create your views here.
class ProfileList(SelectRelatedMixin, ListView):
    model = Profile
    template_name = 'profiles_app/profile_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        result = super(ListView, self).get_queryset()

        if self.request.GET.get('q'):
            query = self.request.GET.get('q')
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(user__username__icontains=q) for q in query_list))
            )
        return result

class ProfileDetail(DetailView):
    model = Profile
    template_name = 'profiles_app/profile_detail.html'

    def get_object(self):
        return get_object_or_404(Profile, user__username=self.kwargs['username'])

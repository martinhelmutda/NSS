### Last modified by César Buenfil on Oct 14,2018

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from django.urls import reverse
from urllib.parse import urlencode
from project_app.models import project, projectImg, project, rolInfo, state, city, category, subcategory
from project_app import models
from django.db.models import Q
from functools import reduce
from django.views import generic
from braces.views import SelectRelatedMixin
import operator
#login
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

#Class Based views
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView, UpdateView,
                                DeleteView)
# Create your views here.

class SearchView(SelectRelatedMixin, generic.ListView):
    template_name = 'search_app/search.html'
    context_object_name = 'projects'
    model = models.project
    select_related = ("pro_category","pro_subcategory", "pro_state", "pro_city")

    def get_queryset(self):
        result = super(ListView, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(pro_name__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(pro_state=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(pro_category=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(pro_city=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(pro_subcategory=q) for q in query_list))

            )
        return result
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['state'] = state.objects.all()
        #context['city'] = city.objects.all()
        #context['subcategory'] = subcategory.objects.all()
        context['category'] = category.objects.all()
        return context

def proper_pagination(posts, index):
    start_index = 0
    end_index = 7
    if posts.number > index:
        start_index = posts.number - index
        end_index = start_index + end_index
    return (start_index, end_index)

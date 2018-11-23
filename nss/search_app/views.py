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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['state'] = state.objects.all()
        context['category'] = category.objects.all()
        return context

    def get_queryset(self):
        result = super(ListView, self).get_queryset()

        if self.request.GET.get('q'):
            query = self.request.GET.get('q')
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(pro_name__icontains=q) for q in query_list))
            )
        if self.request.GET.get('id_pro_category'):
            id_pro_category = self.request.GET.get('id_pro_category')
            query_list = id_pro_category.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(pro_category=id_pro_category) for id_pro_category in query_list))
            )
        if self.request.GET.get('id_pro_subcategory'):
            id_pro_subcategory = self.request.GET.get('id_pro_subcategory')
            query_list = id_pro_subcategory.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(pro_subcategory=id_pro_subcategory) for id_pro_subcategory in query_list))
            )
        if self.request.GET.get('id_pro_state'):
            id_pro_state = self.request.GET.get('id_pro_state')
            query_list = id_pro_state.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(pro_state=id_pro_state) for id_pro_state in query_list))
            )
        if self.request.GET.get('id_pro_city'):
            id_pro_city = self.request.GET.get('id_pro_city')
            query_list = id_pro_city.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(pro_city=id_pro_city) for id_pro_city in query_list))
            )

        if self.request.GET.get('id_pro_group') == 'grupos':
            id_pro_group = self.request.GET.get('id_pro_group')
            result = result.filter(pro_group=True)

        if self.request.GET.get('id_pro_project') == 'proyectos':
            id_pro_project = self.request.GET.get('id_pro_project')
            result = result.filter(pro_group=False)

        return result

def proper_pagination(posts, index):
    start_index = 0
    end_index = 7
    if posts.number > index:
        start_index = posts.number - index
        end_index = start_index + end_index
    return (start_index, end_index)

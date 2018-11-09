from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from .models import Thread, Message
from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.
@method_decorator(login_required, name="dispatch")
class ThreadList(TemplateView):
    template_name="messages_app/thread_list.html"
    # model = Thread
    # def get_queryset(self):
    #     queryset = super(ThreadList, self). get_queryset()
    #     return queryset.filter(users=self.request.user)

        #user.threads.all()

@method_decorator(login_required, name="dispatch")
class ThreadDetail(DetailView):
    model = Thread

    def get_object(self):
        obj = super(ThreadDetail, self).get_object()
        if self.request.user not in obj.users.all():
            raise Http404()
        return obj

def add_message(request, pk):
    json_response = {'created':False}
    if request.user.is_authenticated:
        # ask for contenttypes
        content = request.GET.get('content', None)
        if content:
            # Get hilo
            thread = get_object_or_404(Thread, pk=pk)
            # Authenticated user writes
            message = Message.objects.create(user=request.user, content=content)
            thread.messages.add(message)
            json_response['created'] = True
    else:
        raise Http404("Usted no está autenticado")
    return JsonResponse(json_response)

@login_required
def start_thread(request, username):
    user = get_object_or_404(User, username=username)
    thread = Thread.objects.find_or_create(user, request.user)
    return redirect(reverse_lazy('messages_app:detail',args=[thread.pk]))

from django import template
from project_app.models import Project

register = template.Library()

@register.simple_tag
def get_project_list():
    project_app = Project.objects.all()
    return project_app

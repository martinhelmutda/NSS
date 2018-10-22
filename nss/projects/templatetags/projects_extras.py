from django import template
from projects.models import Project

register = template.Library()

@register.simple_tag
def get_project_list():
    projects = Project.objects.all()
    return projects

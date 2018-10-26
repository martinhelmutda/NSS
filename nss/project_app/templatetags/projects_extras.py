from django import template
from project_app.models import project

register = template.Library()

@register.simple_tag
def get_project_list():
    project_app = project.objects.all()
    return project_app

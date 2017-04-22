from django import template
from landing.models import AboutUs, Data, Visualization


register = template.Library()


@register.assignment_tag
def get_aboutus_tag():
    return AboutUs.objects.first()


@register.assignment_tag
def get_datalist_tag():
    return Data.objects.all().order_by('-id')


@register.assignment_tag
def get_Visualization_tag():
    return Visualization.objects.all().order_by('-id')

@register.assignment_tag
def get_recentVisualization_tag():
    limit = 5
    return Visualization.objects.order_by('-id')[:limit]

@register.assignment_tag
def get_recentDataset_tag():
    limit = 5
    return Data.objects.order_by('-id')[:limit]


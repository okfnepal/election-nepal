from django import template
from landing.models import AboutUs,Data,Visualization
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404


register = template.Library()


@register.assignment_tag
def get_aboutus_tag():
    try:
        aboutus=get_object_or_404(AboutUs,pk=1)

    except:
        aboutus='Some thing Error'


    return aboutus


@register.assignment_tag
def get_datalist_tag():
    try:
        Datalist=Data.objects.all()

    except:
        Datalist='Please Import Data'


    return Datalist


@register.assignment_tag
def get_Visualization_tag():
    try:
        Visualizationlist=Visualization.objects.all()
    except:
        Visualizationlist='Please Import Visualization'


    return Visualizationlist


@register.assignment_tag
def get_recentVisualization_tag():
    try:
        limit = 5
        recentVisualizationlist=Visualization.objects.order_by('id')[:5][::-1]
    except:
        recentVisualizationlist='Please Import Visualization'


    return recentVisualizationlist

@register.assignment_tag
def get_recentDataset_tag():
    try:
        limit = 5
        recentDatasetList=Data.objects.order_by('id')[:5][::-1]
    except:
        recentDatasetList='Please Import Datasets'


    return recentDatasetList


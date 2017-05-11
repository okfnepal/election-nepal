from django.shortcuts import render
from landing.models import Data
from django.db.models import Q
from operator import __or__ as OR

def dataset_preview(request, id):
    template = 'pages/data-preview.html'
    model = Data.objects.get(id=id)
    context = {
        'dataset_id': model
    }
    return render(request, template, context)

def data_filter(request):
    template = 'pages/data-filter.html'
    type = request.GET['type']
    province = request.GET['province']
    district = request.GET['district']
    dataset=''
    if type == 'None' and province=='None' :
        dataset = Data.objects.filter(district=district)
    elif type == 'None' and district=='None':
        dataset = Data.objects.filter(province=province)
    elif province=='None' and district=='None':
        dataset = Data.objects.filter(type=type)
    elif type == 'None':
        dataset = Data.objects.filter(district=district,province=province)
    elif district == 'None':
        dataset = Data.objects.filter(type=type,province=province)
    elif province == 'None':
        dataset = Data.objects.filter(district=district,type=type)
    else :
        dataset = Data.objects.filter(district=district,type=type,province=province)

    context={
        'dataset':dataset,
    }
    return render(request, template, context)
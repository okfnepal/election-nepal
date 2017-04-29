from django.shortcuts import render
from landing.models import Data

def dataset_preview(request, id):
    template = 'pages/data-preview.html'
    model = Data.objects.get(id=id)
    context = {
        'dataset_id': model
    }
    return render(request, template, context)

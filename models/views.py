from django.shortcuts import get_object_or_404, render

from .models import Car
from .filters import CarFilter
from django.core.paginator import Paginator

from models.models import Model, Variant

# Create your views here.
def models_home(request):
    template_name = 'models/home.html'
    if request.method == 'GET':
        objects = Car.objects.all()
        myFilter = CarFilter(request.POST, queryset=objects)
        objects = myFilter.qs
        page_num = request.GET.get('page')
        models_paginator = Paginator(objects, 8)
        page = models_paginator.get_page(page_num)
        context = {"objects": objects, 'myFilter': myFilter, 'count': models_paginator.count, 'page': page}
        return render(request, template_name, context)
    if request.method == 'POST':
        objects = Car.objects.all()
        myFilter = CarFilter(request.POST, queryset=objects)
        objects = myFilter.qs
        page_num = request.GET.get('page')
        models_paginator = Paginator(objects, 8)
        page = models_paginator.get_page(page_num)
        context = {"objects": objects, 'myFilter': myFilter, 'count': models_paginator.count, 'page': page}
        return render(request, template_name, context)
    return render(request, template_name)

def detail(request,id):
    template_name = 'models/details.html'
    if request.method == 'GET':
        car=get_object_or_404(Car,id=id)
        context={'car':car}
        return render(request,template_name,context)
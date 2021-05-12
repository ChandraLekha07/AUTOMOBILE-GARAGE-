from django.shortcuts import render

from .models import Car
from .filters import CarFilter

# Create your views here.
def models_home(request):
    template_name = 'models/home.html'
    if request.method == 'GET':
        objects = Car.objects.all()
        myFilter = CarFilter(request.GET,queryset=objects)
        objects=myFilter.qs
        context = {"objects":objects,'myFilter':myFilter}
    return render(request, template_name, context)
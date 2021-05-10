from django.shortcuts import render

from .models import Car

# Create your views here.
def models_home(request):
    template_name = 'models/home.html'
    if request.method == 'GET':
        objects = Car.objects.all()
        context = {"objects":objects}
    return render(request, template_name, context)
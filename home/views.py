from django.shortcuts import render

# Create your views here.

def render_index(request):
    template_name = 'home/index.html'
    return render(request, template_name)

def render_login(request):
    template_name = 'registration/login.html'
    return render(request, template_name)

def render_signup(request):
    template_name = 'registration/signup.html'
    return render(request, template_name)

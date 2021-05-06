from django.shortcuts import render

from django.views import View
from .models import User
from .forms import UserModelForm

# Create your views here.
def render_index(request):
    template_name = 'home/index.html'
    return render(request, template_name)

def render_login(request):
    template_name = 'registration/login.html'
    return render(request, template_name)

class UserCreateView(View):
    template_name = 'registration/signup.html'

    def get(self, request, *args, **kwargs):
        form = UserModelForm()
        context = {"form":form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = UserModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = UserModelForm()
        # else:
        #     form.errors
        context = {"form":form}
        return render(request, self.template_name, context)
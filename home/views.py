from django.shortcuts import render, reverse


from django.views import View
from .models import User
from .forms import UserModelForm,UserLoginForm

# Create your views here.
def render_index(request):
    template_name = 'home/index.html'
    return render(request, template_name)

class UserCreateView(View):
    template_name = 'registration/signup.html'
    success_url = 'registration/login.html'

    def get(self, request, *args, **kwargs):
        form = UserModelForm()
        context = {"form":form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = UserModelForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, self.success_url)
        context = {"form": form}
        return render(request, self.template_name, context)

class UserLoginView(View):
    template_name = 'registration/login.html'
    success_url = 'home/index.html'

    def get(self, request, *args, **kwargs):
        form = UserLoginForm()
        context = {"form":form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            print("LOGIN SUCCESSFULL")
            return render(request, self.success_url)
        context = {"form": form}
        return render(request, self.template_name, context)

# class UserUpdateView(View):
#     template_name = 'registration/update.html'
#
#     def get(self, request, *args, **kwargs):
#         form = UserModelForm()
#         context = {"form":form}
#         return render(request, self.template_name, context)
#
#     def post(self, request, *args, **kwargs):
#         form = UserModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#         context = {"form": form}
#         return render(request, self.template_name, context)
#
# class UserDeleteView(View):
#     template_name = 'registration/delete.html'
#     success_url = 'registration/login.html'
#
#     def get(self, request, *args, **kwargs):
#         form = UserModelForm()
#         context = {"form":form}
#         return render(request, self.template_name, context)
#
#     def post(self, request, *args, **kwargs):
#         form = UserModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request, self.success_url)
#         context = {"form": form}
#         return render(request, self.template_name, context)

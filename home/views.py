from django.shortcuts import render, reverse
from django.contrib import messages

from django.views import View
from .models import User
from .forms import UserModelForm, UserLoginForm

# Create your views here.
def render_index(request):
    template_name = 'home/index.html'
    if 'username' in request.session:
        return render(request, 'home/home.html')
    return render(request, template_name)

def render_home(request):
    template_name = 'home/home.html'
    if 'username' not in request.session:
        return render(request, 'home/index.html')
    return render(request, template_name)

class UserCreateView(View):
    template_name = 'registration/signup.html'

    def get(self, request, *args, **kwargs):
        if 'username' in request.session:
            return render(request, 'home/home.html')
        form = UserModelForm()
        context = {"form":form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = UserModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Welcome to our family, your account was created successfully!')
            list(messages.get_messages(request))
        context = {"form": form}
        return render(request, self.template_name, context)

class UserLoginView(View):
    template_name = 'registration/login.html'
    success_url = 'home/home.html'

    def get(self, request, *args, **kwargs):
        if 'username' in request.session:
            return render(request, 'home/home.html')
        form = UserLoginForm()
        context = {"form":form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            try:
                form_email = form.cleaned_data['email']
                form_password = form.cleaned_data['password']
                user_obj = User.objects.get(email=form_email)
                if user_obj.password != form_password:
                    messages.info(request, 'passwords do not match')
                    list(messages.get_messages(request))
                else:
                    request.session['username'] = user_obj.email
                    request.user = user_obj.email
                    messages.info(request, 'Welcome You are logged in as')
                    list(messages.get_messages(request))
                    return render(request, self.success_url)
            except User.DoesNotExist:
                messages.info(request, 'User does not exist with given email')
                list(messages.get_messages(request))
        context = {"form": form}
        return render(request, self.template_name, context)
def logout(request):
    if request.method == 'GET':
        try:
            del request.session['username']
            request.session.flush()
        except KeyError:
            pass
        return render(request, 'home/index.html')
    return render(request, 'home/home.html')

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

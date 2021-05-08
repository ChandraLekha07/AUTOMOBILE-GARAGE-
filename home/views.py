from django.shortcuts import render, redirect
from django.contrib import messages

from django.views import View
from .models import User
from .forms import UserModelForm, UserLoginForm, UserViewForm, UserUpdateForm

# Create your views here.
def render_index(request):
    template_name = 'home/index.html'
    return render(request, template_name)

class UserCreateView(View):
    template_name = 'registration/signup.html'

    def get(self, request, *args, **kwargs):
        if 'username' in request.session:
            return redirect('/')
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
    success_url = 'home/index.html'

    def get(self, request, *args, **kwargs):
        if 'username' in request.session:
            return redirect('/')
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
    return redirect('/')

def profile(request):
    template_name = 'registration/profile.html'
    if 'username' in request.session:
        if request.method == 'GET':
            object = User.objects.get(email=request.session.get('username'))
            form = UserViewForm(instance=object)
            context = {"form": form}
            return render(request, template_name, context)
    return redirect('/login')

def update(request):
    template_name = 'registration/update.html'
    if 'username' in request.session:
        if request.method == 'GET':
            object = User.objects.get(email=request.session.get('username'))
            form = UserUpdateForm(instance=object)
            context = {"form": form}
            return render(request, template_name, context)
        if request.method == 'POST':
            object = User.objects.get(email=request.session.get('username'))
            form = UserUpdateForm(request.POST, instance=object)
            if form.is_valid():
                form.save()
                messages.info(request, 'Your account details were updated successfully!')
                list(messages.get_messages(request))
                return redirect('/account')
    return redirect('/login')

def delete(request):
    template_name = 'registration/confirm_delete.html'
    if 'username' in request.session:
        if request.method == 'GET':
            object = User.objects.get(email=request.session.get('username'))
            form = UserViewForm(instance=object)
            context = {"form": form}
            return render(request, template_name, context)
        if request.method == 'POST':
            object = User.objects.get(email=request.session.get('username'))
            object.delete()
            request.session.flush()
            messages.info(request, 'Your account was deleted successfully!')
            list(messages.get_messages(request))
            return render(request, 'home/index.html')
    return redirect('/login')
from django.shortcuts import render, redirect, get_object_or_404

from django.views import View

from .forms import SellCarModelForm

from models.models import Make, Model, Variant
from .models import SellCar
from .filters import ShopCarFilter
from django.core.paginator import Paginator

import smtplib, ssl

# Create your views here.
def render_shop(request):
    template_name = 'shop/home.html'

    if 'username' in request.session:
        return render(request, template_name)
    return redirect('/login')

class SellCreateView(View):
    template_name = 'shop/sell_oldcar.html'
    success_url = 'shop/sell_success.html'

    def get(self, request, *args, **kwargs):
        if 'username' in request.session:
            form = SellCarModelForm()
            context = {"form": form}
            return render(request, self.template_name, context)
        return redirect('/login')

    def post(self, request, *args, **kwargs):
        if 'username' in request.session:
            form = SellCarModelForm(request.POST, request.FILES)
            context = {"form": form}
            if form.is_valid():
                form.save()
                sendMail(request, form)
                form = SellCarModelForm()
                context = {"form": form}
                return render(request, self.success_url, context)
            return render(request, self.template_name, context)
        return redirect('/login')

def load_models(request):
    make_id = request.GET.get('make_id')
    models = Model.objects.filter(make_id=make_id).all()
    return render(request, 'shop/model_dropdown_list_options.html', {'models': models})

def load_variants(request):
    model_id = request.GET.get('model_id')
    variants = Variant.objects.filter(model_id=model_id).all()
    return render(request, 'shop/variant_dropdown_list_options.html', {'variants': variants})

def sendMail(request, form):
    if 'username' in request.session:
        sender = "",
        password = ""
        with open("shop/static/credentials.txt", "r") as f:
            file = f.readlines()
            sender = file[0].strip()
            password = file[1].strip()
        port = 465
        fullname = form.cleaned_data['fullname']
        make = form.cleaned_data['make']
        model = form.cleaned_data['model']
        variant = form.cleaned_data['variant']
        expectedprice = form.cleaned_data['expectedprice']
        receiver = form.cleaned_data['email']
        print(sender, password)
        print(receiver)
        sent_subject = "AMG - Your Care Sale is online"
        sent_body = ("Hello, Mr."+ fullname + " Your automobile sale request for\n"
                    "Make: " + str(make) + "\n"
                    "Model: " + str(model) + "\n"
                    "Variant: " + str(variant) + "\n"
                     "is BOOKED for an initial price of "+ str(expectedprice) +"\n"
                     "Contact dealer for more updates\n"
                     "Team AMG")
        email_text = """\
                From: %s
                To: %s
                Subject: %s

                %s
                """ % (sender, " ".join(receiver), sent_subject, sent_body)
        context = ssl.create_default_context()
        print("Starting to send")
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver, email_text)
        print("Email sent!")
        return
    return redirect('/login')

def render_buy(request):
    template_name = 'shop/buy_oldcar.html'
    if 'username' in request.session:
        if request.method == 'GET':
            objects = SellCar.objects.all()
            myFilter = ShopCarFilter(request.POST, queryset=objects)
            objects = myFilter.qs
            page_num = request.GET.get('page')
            models_paginator = Paginator(objects, 8)
            page = models_paginator.get_page(page_num)
            context = {"objects": objects, 'myFilter': myFilter, 'count': models_paginator.count, 'page': page}
            return render(request, template_name, context)
        if request.method == 'POST':
            objects = SellCar.objects.all()
            myFilter = ShopCarFilter(request.POST, queryset=objects)
            objects = myFilter.qs
            page_num = request.GET.get('page')
            models_paginator = Paginator(objects, 8)
            page = models_paginator.get_page(page_num)
            context = {"objects": objects, 'myFilter': myFilter, 'count': models_paginator.count, 'page': page}
            return render(request, template_name, context)
        return render(request, template_name)
    return redirect('/login')

def product_detail(request,id):
    template_name = 'shop/details.html'
    if request.method == 'GET':
        car = get_object_or_404(SellCar,id=id)
        context = {'car':car}
        return render(request, template_name, context)
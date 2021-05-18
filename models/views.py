from shop.models import BuyCar
from home.models import User, Dealer
from models.forms import DealsModelForm
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import messages

from .models import Car
from .filters import CarFilter
from django.core.paginator import Paginator

from models.models import Model, Variant
import smtplib, ssl

# Create your views here.
def models_home(request):
    template_name = 'models/home.html'
    if request.method == 'GET':
        objects = Car.objects.all()
        myFilter = CarFilter(request.POST, queryset=objects)
        objects = myFilter.qs
        page_num = request.GET.get('page')
        models_paginator = Paginator(objects, 2)
        page = models_paginator.get_page(page_num)
        context = {"objects": objects, 'myFilter': myFilter, 'count': models_paginator.count, 'page': page}
        return render(request, template_name, context)
    if request.method == 'POST':
        objects = Car.objects.all()
        myFilter = CarFilter(request.POST, queryset=objects)
        objects = myFilter.qs
        page_num = request.GET.get('page')
        models_paginator = Paginator(objects, 2)
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
    if request.method == 'POST':
        if 'username' in request.session:
            form = DealsModelForm(request.POST)
            context = {"form": form}
            car = get_object_or_404(Car, id=id)
            dealer = get_object_or_404(Dealer, id=id)
            buyer = User.objects.get(email=request.session.get('username'))

            info = {}
            info['car'] = car
            info['dealer'] = dealer
            info['buyer'] = buyer

            if form.is_valid():
                att = form.save(commit=False)
                att.car = info['car']
                att.dealer = info['dealer']
                att.buyer = info['buyer']
                form.save()
                mailBuyer(request, info)
                mailDealer(request, info)
                messages.info(request, 'You have booked a Deal Check your gmail for more info')
                list(messages.get_messages(request))
                form = DealsModelForm()
                context = {"form": form}
                return render(request, template_name, context)
            return render(request, template_name, context)
        return redirect('/login')

def mailBuyer(request, info):
    if 'username' in request.session:
        sender = "",
        password = ""
        with open("shop/static/credentials.txt", "r") as f:
            file = f.readlines()
            sender = file[0].strip()
            password = file[1].strip()
        port = 465
        make = info['car'].make
        model = info['car'].model
        variant = info['car'].variant
        fuel = info['car'].fuel
        price = info['car'].price
        name = info['dealer'].name
        mobile = info['dealer'].mobile
        state = info['dealer'].state
        city = info['dealer'].city
        address = info['dealer'].address
        email = info['dealer'].email
        receiver_name = info['buyer'].firstname + ' ' + info['buyer'].lastname
        receiver = info['buyer'].email
        sent_body = ("Hello, Mr./Ms."+ receiver_name + " Your deal is booked for the following car \n"
                    "Make: " + str(make) + "\n"
                    "Model: " + str(model) + "\n"
                    "Variant: " + str(variant) + "\n"
                    "Fuel: " + str(fuel) + "\n"
                    "Price: "+ str(price) +"\n"+"\n"
                    "Contact : " + "\n"
                    "Dealer name: " + str(name) + "\n"
                    "Mobile: " + str(mobile) + "\n"
                    "Email: " + str(email) + "\n"
                    "State: " + str(state) + "\n"
                    "City: " + str(city) + "\n"
                    "Address: " + str(address) + "\n"
                     "\n"
                     "Team AMG")
        email_text = """\From: %s

                %s
                """ % (sender,  sent_body)
        context = ssl.create_default_context()
        print("Starting to send to buyer")
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver, email_text)
        print("Email sent to buyer!")
        return
    return redirect('/login')

def mailDealer(request, info):
    if 'username' in request.session:
        sender = "",
        password = ""
        with open("shop/static/credentials.txt", "r") as f:
            file = f.readlines()
            sender = file[0].strip()
            password = file[1].strip()
        port = 465
        price = info['car'].price
        name = info['buyer'].firstname + ' ' + info['buyer'].lastname
        mobile = info['buyer'].mobile
        state = info['buyer'].state
        city = info['buyer'].city
        email = info['buyer'].email
        receiver_name = info['dealer'].name
        receiver = info['dealer'].email
        sent_body = (
                    "\n" + "\n"
                    "Contact : " + "\n"
                    "Buyer name: " + str(name) + "\n"
                    "Mobile: " + str(mobile) + "\n"
                    "Email: " + str(email) + "\n"
                    "State: " + str(state) + "\n"
                    "City: " + str(city) + "\n"
                    "\n"
                    "Team AMG")

        email_text = """\From: %s
                %s
                """ % (sender,  sent_body)
        context = ssl.create_default_context()
        print("Starting to send to dealer")
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver, email_text)
        print("Email sent to dealer!")
        return
    return redirect('/login')
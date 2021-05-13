from django.shortcuts import render, redirect

from django.views import View

from .forms import SellCarModelForm

from models.models import Make, Model, Variant

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
        name = form.cleaned_data['name']
        variant = form.cleaned_data['variant']
        expectedprice = form.cleaned_data['expectedprice']
        receiver = form.cleaned_data['email']
        print(sender, password)
        print(receiver)
        sent_subject = "AMG - Your Care Sale is online"
        sent_body = ("Hello, Mr."+ fullname + " Your automobile sale request for\n"
                     "Make: " + make + "\n"
                     "Model: " + name + "\n"
                     "Variant: " + variant + "\n"
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
        return render(request, template_name)
    return redirect('/login')

def render_exchange(request):
    template_name = 'shop/exchange_car.html'
    if 'username' in request.session:
        return render(request, template_name)
    return redirect('/login')

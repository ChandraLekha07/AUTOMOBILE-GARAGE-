from django.shortcuts import render, redirect

from django.views import View

from .forms import SellCarModelForm

from home.models import User

import random
import math
from twilio.rest import Client

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
        form = SellCarModelForm()
        context = {"form": form}
        try:
            username = request.session['username']
            user_obj = User.objects.get(email=username)
            mobile = user_obj.mobile
            print('Mobile: ',mobile)
            values = "0123456789abcdefghijklmnoqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            l = len(values)
            otp = ""
            for i in range(6):
                otp += values[math.floor(random.random() * l)]
            message = "Your otp is " + otp
            account_sid = 'ACf6ee7d1ba7bd910fcc69246d9f0de6fb'
            auth_token = 'aaa5eb8ea4e3d59767add19b3ca303b9'
            client = Client(account_sid, auth_token)
            message = client.messages \
                .create(
                body=str(message),
                from_='+18575870863',
                to='+91' + str(mobile)
            )
            print('OTP: ', otp)
            print('MESSAGE.SID: ', message.sid)
        except KeyError:
            return redirect('/login')
        except:
            print('OTP SEND FAILED')
            return render(request, self.template_name)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        if request.session['username']:
            form = SellCarModelForm(request.POST)
            if form.is_valid():
                #form.save()
                # mobile = form.cleaned_data['mobile']
                # context = {"mobile": mobile}
                return render(request, self.success_url)
            return render(request, self.template_name)
        return redirect('/login')

def render_buy(request):
    template_name = 'shop/buy_oldcar.html'
    # if 'username' in request.session:
    return render(request, template_name)
    # return redirect('/login')

def render_exchange(request):
    template_name = 'shop/exchange_car.html'
    # if 'username' in request.session:
    return render(request, template_name)
    # return redirect('/login')

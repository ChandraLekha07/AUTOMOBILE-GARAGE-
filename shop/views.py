from django.shortcuts import render, redirect

# Create your views here.
def render_shop(request):
    template_name = 'shop/home.html'
    if 'username' in request.session:
        return render(request, template_name)
    return redirect('/login')

def render_sell(request):
    template_name = 'shop/sell_oldcar.html'
    if 'username' in request.session:
        return render(request, template_name)
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

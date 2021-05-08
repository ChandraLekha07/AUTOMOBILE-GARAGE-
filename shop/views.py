from django.shortcuts import render

# Create your views here.
def render_shop(request):
    #if user logged in
    return render(request, 'shop/home.html')
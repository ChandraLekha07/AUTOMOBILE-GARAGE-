from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_index, name="index"),
    path('login/', views.render_login, name="login"),
    path('signup/', views.render_signup, name="signup"),
]
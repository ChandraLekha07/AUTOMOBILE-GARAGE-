from django.urls import path
from .views import (
    render_index,
    render_login,
    UserCreateView
)

urlpatterns = [
    path('', render_index, name="index"),
    path('login/', render_login, name="login"),
    path('signup/', UserCreateView.as_view(), name="signup"),
]
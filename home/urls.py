from django.urls import path
from .views import (
    render_index,
    render_login,
    UserCreateView,
    # UserUpdateView,
    # UserDeleteView
)

urlpatterns = [
    path('', render_index, name="index"),
    path('login/', render_login, name="login"),
    path('signup/', UserCreateView.as_view(), name="signup"),
    # path('account/update/', UserUpdateView.as_view(), name="account-update"),
    # path('account/delete/', UserDeleteView.as_view(), name="account-delete"),
]
from django.urls import path
from .views import (
    render_index,
    UserCreateView,
    UserLoginView,
    render_home,
    logout,
    # UserUpdateView,
    # UserDeleteView
)

urlpatterns = [
    path('', render_index, name="index"),
    path('signup/', UserCreateView.as_view(), name="signup"),
    path('login/', UserLoginView.as_view(), name="login"),
    path('home/', render_home, name="user-home"),
    path('logout/', logout, name="logout"),
    # path('account/update/', UserUpdateView.as_view(), name="account-update"),
    # path('account/delete/', UserDeleteView.as_view(), name="account-delete"),
]
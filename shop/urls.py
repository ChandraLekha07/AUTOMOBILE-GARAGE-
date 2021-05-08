from django.urls import path
from .views import (
    render_shop,
)

urlpatterns = [
    path('', render_shop, name="shop-home"),
]
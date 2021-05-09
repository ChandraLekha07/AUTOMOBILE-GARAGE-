from django.urls import path
from .views import (
    render_shop,
    render_sell,
    render_buy,
    render_exchange,
)

urlpatterns = [
    path('', render_shop, name="shop-home"),
    path('sell', render_sell, name="shop-sell"),
    path('buy', render_buy, name="shop-buy"),
    path('exchange', render_exchange, name="shop-exchange"),
]
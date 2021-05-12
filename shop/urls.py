from django.urls import path
from .views import (
    render_shop,
    SellCreateView,
    render_buy,
    render_exchange,
)

urlpatterns = [
    path('', render_shop, name="shop-home"),
    path('sell', SellCreateView.as_view(), name="shop-sell"),
    path('buy', render_buy, name="shop-buy"),
    path('exchange', render_exchange, name="shop-exchange"),
]
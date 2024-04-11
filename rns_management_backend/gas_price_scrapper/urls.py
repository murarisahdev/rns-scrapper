from django.urls import path

from .views import GasPriceListView

urlpatterns = [
        path('gas-prices/', GasPriceListView.as_view(), name='gas-price-list'),
]

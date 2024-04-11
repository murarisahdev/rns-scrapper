from rest_framework import generics

from .models import GasPrice
from .serializers import GasPriceSerializer


class GasPriceListView(generics.ListAPIView):
    """
    View for listing gas prices.
    """
    queryset = GasPrice.objects.all().order_by('-timestamp')
    serializer_class = GasPriceSerializer
    
    def get_queryset(self):
        return super().get_queryset()

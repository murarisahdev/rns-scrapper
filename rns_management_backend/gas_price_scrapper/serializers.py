from rest_framework import serializers

from .models import GasPrice


class GasPriceSerializer(serializers.ModelSerializer):
    """
    Serializer for GasPrice model.
    """
    class Meta:
        model = GasPrice
        fields = '__all__'

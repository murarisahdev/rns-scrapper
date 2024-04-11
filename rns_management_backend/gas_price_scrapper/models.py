from django.db import models


class GasPrice(models.Model):
    price = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

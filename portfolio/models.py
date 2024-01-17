from django.db import models

# Create your models here.
class Bank_Account(models.Model):
    name = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

class Equity(models.Model):
    ticker = models.CharField(max_length=10)
    shares = models.PositiveIntegerField()
    average_price_per_share = models.DecimalField(max_digits=10, decimal_places=2)
    date_purchased = models.DateField()
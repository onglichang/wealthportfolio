from rest_framework import serializers
from .models import Bank_Account

class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank_Account
        fields = '__all__'


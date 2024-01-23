from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Bank_Account, Equity
from .utils import getEquityCurrentPrice
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import BankAccountSerializer

# Create your views here.
def portfolio_list(request):
    bank_account_list = Bank_Account.objects.all()
    equity_list = Equity.objects.all()
    price_list = {}
    for equity in equity_list:
        equity.current_price_per_share = getEquityCurrentPrice(equity.ticker)
    template = loader.get_template('portfolio_list.html')
    context = {
        'bank_account_list': bank_account_list,
        'equity_list': equity_list,
    }
    return HttpResponse(template.render(context, request))
    # return render(request, 'portfolio/portfolio_list.html', {'cash_list': cash_list, 'equity_list': equity_list})

# REST APIs
@api_view(['GET', 'POST'])
def bank_accounts_list(request, format=None):
    """
    List all user's bank accounts, or create a new bank account.
    """
    if request.method == 'GET':
        bank_accounts = Bank_Account.objects.all()
        serializer = BankAccountSerializer(bank_accounts, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = BankAccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def add_bank_account(request):
#     serializer = BankAccountSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)
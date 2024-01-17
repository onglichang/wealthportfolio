from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Bank_Account, Equity

# Create your views here.
def portfolio_list(request):
    bank_account_list = Bank_Account.objects.all()
    equity_list = Equity.objects.all()
    template = loader.get_template('portfolio_list.html')
    context = {
        'bank_account_list': bank_account_list,
        'equity_list': equity_list
    }
    return HttpResponse(template.render(context, request))
    # return render(request, 'portfolio/portfolio_list.html', {'cash_list': cash_list, 'equity_list': equity_list})
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import portfolio_list, bank_accounts_list

urlpatterns = [
    path('portfolio/', portfolio_list, name='portfolio_list'),
    path('banks/', bank_accounts_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)
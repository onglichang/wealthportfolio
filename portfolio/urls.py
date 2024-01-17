from django.urls import path
from .views import portfolio_list

urlpatterns = [
    path('portfolio/', portfolio_list, name='portfolio_list'),
]
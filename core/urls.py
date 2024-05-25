# core/urls.py

from django.urls import path
from core import views

urlpatterns = [
    path('api/accounts/', views.AccountListAPIView.as_view(), name='account-list'),
    path('api/destinations/', views.DestinationListAPIView.as_view(), name='destination-list'),
    path('api/destinations/<uuid:account_id>/', views.DestinationByAccountAPIView.as_view(), name='destination-by-account'),
]
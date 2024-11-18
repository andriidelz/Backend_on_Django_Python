from django.urls import path
from . import views

urlpatterns = [
    path('currency/', views.currency_list, name='currency_list'),
]

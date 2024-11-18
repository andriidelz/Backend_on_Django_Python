from django.shortcuts import render
from django.http import JsonResponse

def currency_list(request):
    data = {'currency': 'Bitcoin', 'price': 25000}
    return JsonResponse(data)

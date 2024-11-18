from django.http import JsonResponse
from django.conf import settings

import asyncio

from backend_project.__init__ import CMCHTTPClient
from django.shortcuts import render

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_project.settings')
application = get_wsgi_application()

cmc_client = CMCHTTPClient(
    base_url="https://pro-api.coinmarketcap.com",
    api_key=settings.CMC_API_KEY
)
    
def test_key(request):
    return JsonResponse({"CMC_API_KEY": settings.CMC_API_KEY})

def get_cryptocurrencies(request):
    listings = asyncio.run(cmc_client.get_listings())
    return JsonResponse(listings, safe=False)

def get_cryptocurrency(request, currency_id):
    currency = cmc_client.get_currency(currency_id)
    return JsonResponse(currency)

def home(request):
    return render(request, 'base.html')

async def get_cryptocurrencies(request):
    listings = await cmc_client.get_listings()
    return JsonResponse(listings, safe=False)

async def get_cryptocurrency(request, currency_id):
    currency = await cmc_client.get_currency(currency_id)
    return JsonResponse(currency)

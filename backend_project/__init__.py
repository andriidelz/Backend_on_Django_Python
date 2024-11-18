import requests
from cachetools import cached, TTLCache

class HTTPClient:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key
        self.headers = {
            'X-CMC_PRO_API_KEY': api_key
        }

    def get(self, url: str, params: dict = None):
        response = requests.get(self.base_url + url, headers=self.headers, params=params)
        return response.json()

class CMCHTTPClient(HTTPClient):
    def __init__(self, base_url: str, api_key: str):
        super().__init__(base_url, api_key)

    @cached(cache=TTLCache(maxsize=100, ttl=300))
    def get_listings(self):
        return self.get("/v1/cryptocurrency/listings/latest")["data"]

    @cached(cache=TTLCache(maxsize=100, ttl=300))
    def get_currency(self, currency_id: int):
        return self.get("/v2/cryptocurrency/quotes/latest", {"id": currency_id})["data"][str(currency_id)]

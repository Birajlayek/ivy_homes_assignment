import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
    
    def get_autocomplete(self, query):
        url = f"{self.base_url}/v1/autocomplete?query={query}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

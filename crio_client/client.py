# Core HTTP client class handling sessions & headers (centralizes error handling, timeouts, and authentication tokens to avoid repeating code across different)
# Encapsulates HTTP transport layer (using requests)
import os 
import requests

class CrioAPIClient:
    def __init__(self, base_url: str = None, api_key: str = None):
        self.base_url = base_url or os.getenv("CRIO_BASE_URL")
        self.api_key = api_key or os.getenv("CRIO_API_KEY")
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json"
        })
        
    def request(self, method:str, endpoint:str, **kwargs):
        url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        response = self.session.request(method, url, **kwargs)
        response.raise_for_status()
        return response.json()
#entry point to communicate with CRIO API
import os 
from crio_client/config impot Config

class CrioClient:
    def __init__(self, token:str=None, base_url:str=None):
        self.base_url = (base_url or Config.BASE_URL).rstrip("/") #--> checks which url to use before applying strip method
        self.token = token or Config.BEARER_TOKEN
        
        # session w/header
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json"
        })
        
    def request(self, method:str, endpoint:str, **kwargs) -> dict:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.request(
            method,
            url,
            # timeout=Config.TIMEOUT,
            **kwargs)
        response.raise_for_status()
        return response.json()
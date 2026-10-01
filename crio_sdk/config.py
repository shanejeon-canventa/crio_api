import os
from dotenv import load_dotenv

load_dotenv()

# env variables & settings mgmt
class Config:
    def __init__(self):
        # Defaults to sandbox unless PROD specified
        self.env = os.getenv("CRIO_ENV", "sandbox").lower()
        
        if self.env == "production":
            self.api_token = os.getenv("PROD_BEARER_TOKEN")
            self.base_url = os.getenv("PROD_BASE_URL")
            self.client_id = os.getenv("PROD_CLS_CLIENT_ID")
            self.site_id = os.getenv("PROD_SITE_ID") #Canventa Mansfield
            
        else:
            self.api_token = os.getenv("SANDBOX_API_TOKEN")
            self.base_url = os.getenv("SANDBOX_BASE_URL")
            self.client_id = os.getenv("SANDBOX_CLS_CLIENT_ID")
            self.site_id = os.getenv("SANDBOX_SITE_ID")
            
        self.timeout = 30 # place holder seconds
        
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_token}", # Expires after 90 days
            "Accept": "application/json"
        }
        
    def get_headers(self) -> dict:
        """Returns CRIO required headers.""" 
        return self.headers.copy() 
        # .copy() provides a "fresh copy" of headers dictionary. Prevents HTTP client/external scripts from modifying/corrupting global default config during run time [vs. returning original]
    
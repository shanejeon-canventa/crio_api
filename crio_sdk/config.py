import os
from dotenv import load_dotenv

load_dotenv()

class Site(str, Enum):
    """Loads all site IDs"""
    MANSFIELD_PROD = os.getenv("SITE_ID_PROD")
    API_SANDBOX = os.getenv("SITE_ID_SANDBOX")
    
# env variables & settings mgmt
class Config:
    def __init__(self):
        # Defaults to sandbox unless PROD specified
        self.env = os.getenv("CRIO_ENV", "sandbox").lower()
        
        if self.env == "production":
            self.api_token = os.getenv("BEARER_TOKEN_PROD")
            self.base_url = os.getenv("BASE_URL_PROD")
            self.client_id = os.getenv("CLIENT_ID_PROD")
            self.site_id = os.getenv("SITE_ID_PROD", site.MANSFIELD_PROD) #Canventa Mansfield
            
        else:
            self.api_token = os.getenv("API_TOKEN_SANDBOX")
            self.base_url = os.getenv("BASE_URL_SANDBOX")
            self.client_id = os.getenv("CLIENT_ID_SANDBOX")
            self.site_id = os.getenv("SITE_ID_SANDBOX", site.API_SANDBOX)
            
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
    
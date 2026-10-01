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
        prefix = "PROD" if self.env == "production" else "SANDBOX"
        
        self.api_token = os.getenv(f"BEARER_TOKEN_{prefix}")
        self.base_url = os.getenv(f"BASE_URL_{prefix}")
        self.client_id = os.getenv(f"CLIENT_ID_{prefix}")
        
        self.site_id_sandbox = os.getenv(f"SITE_ID_SANDBOX")  
        self.site_id_mansfield = os.getenv(f"SITE_ID_CM_PROD")
            
        self.timeout = 30 # 30 seconds
        
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_token}", # Expires after 90 days
            "Accept": "application/json"
        }
        
    def get_headers(self) -> dict:
        """Returns CRIO required headers.""" 
        return self.headers.copy() 
        # preserves original, prevents mutation 
    
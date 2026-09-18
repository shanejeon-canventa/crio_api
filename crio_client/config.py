import os

# env variables & settings mgmt
class Config:
    def __init__(self):
        self.api_token = os.getenv("CRIO_API_TOKEN")
        self.base_url = os.getenv("CRIO_BASE_URL")
        self.client_id = os.getenv("CLS_CLIENT_ID")
        self.site_id = os.getenv("SITE_ID") # for Canventa Mansfield
        self.timeout = 30 # place holder seconds
        
        self.required_headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_token}", # Expires after 90 days
            "Accept": "application/json"
        }
        
    def get_headers(self) -> dict:
        """Returns CRIO required headers.""" 
        headers = self.required_headers.copy() 
        # .copy() provides a "fresh copy" of headers dictionary. Prevents HTTP client/external scripts from modifying/corrupting global default config during run time [vs. returning original]
        
        return headers
    
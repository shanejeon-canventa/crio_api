import os
import json
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
    
def load_json_data(conf_json_name:str="conf.json") -> dict:
    config_path = Path(conf_json_name)
    # if not conf_json_name.exists():
    #     raise FileNotFoundError(f"conf.json file missing: {config_path}")
    
    with open(config_path, mode="r", encoding="utf-8-sig") as data:
        return json.load(data)
    
# env variables & settings mgmt
class Config:
    def __init__(self):
        env_var = os.getenv("CRIO_ENV")
        self.is_production = env_var is not None and env_var.strip().lower() == "production"
        self.env = os.getenv("CRIO_ENV", "sandbox").lower()
        suffix = "PROD" if self.env == "production" else "SANDBOX"
        
        self.api_token = os.getenv(f"BEARER_TOKEN_{suffix}")
        self.base_url = os.getenv(f"BASE_URL_{suffix}")
        self.client_id = os.getenv(f"CLIENT_ID_{suffix}")
        self.site_id = os.getenv(f"SITE_ID_{suffix}")        
            
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

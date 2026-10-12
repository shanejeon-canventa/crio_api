import os
import json
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
    
# env variables & settings mgmt
class Config:
    def __init__(self, config_path:str="conf.json"):
        self.config_path = Path(config_path)
        self.config_data = self._load_config()
        
        self.env = os.getenv("CRIO_ENV", "sandbox").lower()
        self.is_production = self.env is not None and self.env.strip().lower() == "production"
        
        env_config = self.config_data.get(self.env, {})
        suffix = "PROD" if self.env == "production" else "SANDBOX"
        self.api_token = os.getenv(f"BEARER_TOKEN_{suffix}")
        self.base_url = os.getenv(f"BASE_URL_{suffix}")
        self.client_id = os.getenv(f"CLIENT_ID_{suffix}")
        self.site_id = os.getenv(f"SITE_ID_{suffix}")        
        
        self.dummy_data_path = self.config_data.get("dummy_data_path")
            
        self.timeout = 30 # 30 seconds
        
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_token}", # Expires after 90 days
            "Accept": "application/json"
        }
    
    def _load_config(self)->dict:
        """Read and parse JSON file"""
        with open(self.config_path, "r", encoding="utf-8-sig") as f:
            return json.load(f)
        
    def get_headers(self) -> dict:
        """Returns CRIO required headers.""" 
        return self.headers.copy() 
        # preserves original, prevents mutation 
        
    def get_file_path(self)->str:
        """Returns file path"""
        return self.dummy_data_path
    
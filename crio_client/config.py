# Configuration loader. Avoids hardcoding
import os 
from dotenv import load_dotenv

# Loading variables from .env file to os.environ
load_dotenv()

class Config:
    # config for SANDBOX API
    BASE_URL: str = os.getenv("BASE_URL")
    BEARER_TOKEN: str = os.getenv("API_KEY")
    # TIMEOUT:int = int(os.getenv("CRIO_TIMEOUT", "30"))
    
    @classmethod
    def validate(cls):
        """Validate bearer token"""
        if not cls.BEARER_TOKEN:
            raise ValueError("CRIO_BEARER_TOKEN is missing from .env")

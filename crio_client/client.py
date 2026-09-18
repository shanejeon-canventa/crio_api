import requests 
from .config import Config 

class CrioAPIError(Exception):
    """Raises error message for API failures"""
    def __init__(self, message:str, status_code:int=None, response_body:dict=None):
        super().__init__(message)
        self.status_code = status_code
        self.response_body = response_body
        
    def __repr__(self):
        return f"CrioAPIError (status_code={self.status_code}, message={super().__str__()!r})"
        
class CrioClient(self):
    def __init__(self, config:Config):
        self.config = config
        
        self.session = requests.Session() # using .get() creates Network Overhead Latency (extra delay to data transmission) and redundancy
        self.session.headers.update(config.get_headers())
        
    def request(self, method:str, endpoint:str, payload:dict=None, params:dict=None)->dict:
        """Centralized HTTP request, GET/POST/PUT/DELETE/etc."""
        url = f"{self.config.base_url}/{endpoint.lstrip('/')}"

        try:
            response = self.session.request(
                method=method,
                url=url,
                json=payload,
                params=params,
                timeout=self.config.timeout        
            )
            response.raise_for_status()
            
            if response.status_code == 204:
                return {}
            
            return response.json()

        except requests.exceptions.HTTPError as err:
            status = getattr(err.response, "status_code", None)
            body = None
            
            if err.response:
                body = err.response.json() 
            raise CrioAPIError(str(err), status_code=status, response_body=body) from err
            

            
            
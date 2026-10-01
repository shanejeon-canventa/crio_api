import requests 
from .config import Config 
from .exceptions import CrioAPIError

class CrioClient:
    def __init__(self, config:Config):
        self.config = config
        self.session = requests.Session() 
        self.session.headers.update(config.get_headers())
        
    def request(
        self, 
        method:str, 
        endpoint:str, 
        payload:dict=None, 
        params:dict=None,
        site_id:str=None
    )->dict:
        """Centralized HTTP request, GET/POST/PUT/DELETE/etc."""
        url = f"{self.config.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        
        query_params = {"client_id": self.config.client_id}

        if site_id:
            query_params["site_id"] = site_id
        
        if params:
            query_params.update(params)
        try:
            response = self.session.request(
                method=method,
                url=url,
                json=payload,
                params=query_params,
                timeout=self.config.timeout        
            )
            response.raise_for_status()
            
            if response.status_code == 204:
                return {}
            
            return response.json()

        except requests.RequestException as err:
            status = getattr(err.response, "status_code", None)
            body = None
            
            if err.response:
                body = err.response.json() 
            raise CrioAPIError(str(err), status_code=status, response_body=body) from err
            

            
            
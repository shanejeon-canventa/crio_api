# Specific API endpoints (e.g., donors, studies, etc.)

class ResourceService:
    def __init__(self, client):
        self.client = client
    
    def get_resource(self, response_id:str):
        return self.client.request('GET', f'/resources/{resource_id}')
    
    def create_resource(self, payload:dict):
        return self.client.request("POST", "/resources", json=payload)
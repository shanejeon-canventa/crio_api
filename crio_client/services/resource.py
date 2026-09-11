# Specific API endpoints (e.g., donors, studies, etc.)
from crio_client.config import Config
from crio_client.client import CrioClient

class ResourceService:
    def __init__(self, client:CrioClient):
        self.client = client
    
    def create_patient(self, payload:dict):
        return self.client.request("POST", f"/api/v1/patient?client_id={Config.CLIENT_ID}", json=payload)
    
    def update_patient(self, payload:dict):
        return self.client.request('PUT', f"/api/v1/patient/{payload.patient_id}?client_id={Config.CLIENT_ID}")
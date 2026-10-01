from .client import CrioClient 

class DonorResource:
    """Handles CRIO 'Patient' endpoints, mapped to CLS Donor terminology"""
    def __init__(self, client: CrioClient):
        self.client = client 
        
    def create_donor(self, donor_data: dict, site_id:str=None) -> dict:
        """Creates new donor record through Patient API"""
        
        endpoint = f"/patient"
        return self.client.request("POST", endpoint, payload=donor_data)

    
    def get_donor_by_id(self, patient_id:str, site_id:str=None)->dict:
        """Retrieves donor by Patient ID."""
        
        endpoint = f"/patient/{patient_id}/site/{site_id}"
        return self.client.request("GET", endpoint)
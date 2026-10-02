from .client import CrioClient 
from .endpoints import PatientEndpoints

class DonorResource:
    """Handles CRIO 'Patient' endpoints, mapped to CLS Donor terminology"""
    def __init__(self, client: CrioClient):
        self.client = client 
        
    def create_donor(self, donor_data: dict) -> dict:
        """Creates new donor record through Patient API"""
        
        return self.client.request("POST", PatientEndpoints.CREATE(), payload=donor_data)
    
    def get_donor_by_id(self, patient_id:str, site_id:str=None)->dict:
        """Retrieves donor by Patient ID through Patient Lookup API"""
        
        return self.client.request("GET", PatientEndpoints.LOOKUP(patient_id, site_id))
    
    def search_donor(self, search_payload: dict, site_id: str=None)->dict:
        """Gets required donor data for patient POST requests."""
        return self.client.request("POST", PatientEndpoints.GET_CONTACT_DATA(), payload=search_payload, site_id=site_id)
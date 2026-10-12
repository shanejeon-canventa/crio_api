from .client import CrioClient 
from .endpoints import PatientEndpoints, StudyEndpoints

class DonorResource:
    """Handles CRIO 'Patient' endpoints, mapped to CLS Donor terminology"""
    def __init__(self, client: CrioClient):
        self.client = client 
        
    def create_donor(self, donor_data: dict) -> dict:
        """Creates new donor record through Patient API"""
        
        return self.client.request("POST", PatientEndpoints.CREATE(), json=donor_data)
    
    def get_donor_by_id(self, patient_id:str, site_id:str=None)->dict:
        """Retrieves donor by Patient ID through Patient Lookup API"""
        
        return self.client.request("GET", PatientEndpoints.LOOKUP_ID(patient_id, site_id))
    
    def get_donor_by_contact(self, contact_info: dict)->dict:
        """Retrieves donor by Contact Info when Patient ID not available through Patient Lookup API"""
        payload = {k: v for k, v in contact_info.items() if v is not None}
        return self.client.request("POST", PatientEndpoints.LOOKUP_CONTACT(), json=payload)
        
class StudyResource:
    """Handles CRIO "Study" endpoints"""
    def __init__(self, client:CrioClient):
        self.client = client 
        
    def get_study_by_id(self, study_id:str)->dict:
        return self.client.request("GET", StudyEndpoints.GET_STUDY_BY_ID(study_id))
    
    def get_study_trait(self, study_id:str)->dict:
        return self.client.request("GET", StudyEndpoints.GET_PROCEDURE_TRAIT_BY_STUDY(study_id))
    
    def get_site_trait(self)->dict:
        return self.client.request("GET", StudyEndpoints.GET_PROCEDURE_TRAIT_BY_SITE())
class PatientEndpoints:
    """For 'Patient' endpoints."""
    
    @staticmethod
    def CREATE() -> str:
        return "/patient"
    
    @staticmethod
    def LOOKUP(patient_id: str, site_id: str) -> str:
        return f"/patient/{patient_id}/site/{site_id}"
    
    
class StudyEndpoints:
    """For 'Study' endpoints."""
    
    @staticmethod
    def GET_TRAIT_STUDY(study_id:str, client_id:str):
        return f"/study/{study_id}/procedure"
    
    def GET_TRAIT_SITE(site_id:str, client_id:str):
        return f"/site/{site_id}/procedure"
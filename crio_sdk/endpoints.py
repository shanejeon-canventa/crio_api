from .config import Config 

config = Config()
site_id = config.site_id

class PatientEndpoints:
    """For 'Patient' endpoints."""
    @staticmethod
    def CREATE() -> str:
        return "/patient"
    
    @staticmethod
    def LOOKUP_ID(patient_id: str) -> str:
        return f"/patient/{patient_id}/site/{site_id}"
    
    @staticmethod 
    def LOOKUP_CONTACT()->str:
        return f"/search/patient"
    
    
class StudyEndpoints:
    """For 'Study' endpoints."""
    @staticmethod
    def GET_STUDY_BY_ID(study_id: str) -> str:
        return f"/study/{study_id}/site/{site_id}"
    @staticmethod
    
    def GET_PROCEDURE_TRAIT_BY_STUDY(study_id:str) -> str:
        """STUDY API"""
        return f"/study/{study_id}/procedure"
    
    @staticmethod
    def GET_PROCEDURE_TRAIT_BY_SITE() -> str:
        return f"/site/{site_id}/procedure"
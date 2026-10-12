from dataclasses import dataclass, field
from typing import Optional, Dict, Any, List
from .config import Config 

def _get_default_site_id()->str:
    """Lazy-load Config, prevent circular import loops during mod load"""
    return Config().site_id

@dataclass 
class DonorPayload:
    first_name: str
    last_name: str
    dob: str
    did: str
    email: str
    homePhone: str="714-681-6473"
    status: str="AVAILABLE"
    notes: str="see legacy notes"
    patient_id: Optional[str] = None 
    site_id: str = field(default_factory=_get_default_site_id)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any])->"DonorPayload":
        """Parses raw JSON data matching API structure into DonorPayload instance"""
        patient_info=data.get("patientInfo", {})
        contact = patient_info.get("patientContact", {})
        
        return cls(
            site_id=data.get("siteId"),
            patient_id=None,
            did=patient_info.get("externalId", ""),
            dob=patient_info.get("birthDate", ""),
            status=patient_info.get("status", "AVAILABLE"),
            notes=patient_info.get("notes", "see legacy notes"),
            first_name=contact.get("firstName", ""),
            last_name=contact.get("lastName", ""),
            email=contact.get("email", ""),
            homePhone=contact.get("homePhone", "")
        )
        
    @classmethod
    def from_list(cls, data_list: List[Dict[str, Any]])-> List["DonorPayload"]:
        return [cls.from_dict(item) for item in data_list]
        
    def to_dict(self)->Dict[str, Any]:
        """Converts DonorPayload instance back into API payload dictionary formatting"""
        return {
        "siteId": self.site_id,
        "patientInfo": {
            "patientId": self.patient_id,
            "externalId": self.did,
            "birthDate": self.dob,
            "status": self.status, 
            "notes": self.notes,
            "patientContact": {
                "firstName": self.first_name,
                "lastName": self.last_name,
                "email": self.email,
                "homePhone": self.homePhone
            }
        }
    } 

    
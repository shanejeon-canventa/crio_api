from .config import load_json_data, Config

def patient_lookup_payload(site_id:str, donor_id:str):
    return {
        "site_id": site_id, 
        "patientInfo": {
        "patientId": donor_id
    }}
    
def patient_payload(donor_id:str, site_id:str, firstName:str, lastName:str, email:str, **kwargs):
    conf = Config()
    conf_data = load_json_data()
    
    payload = {
        "siteId": siteId,
        "patientInfo": {
            "patientId": donor_id,
            "status": "AVAILABLE"
        },
        "patientContact": {
            "firstName": firstName,
            "lastName": lastName,
            "email": email            
        }
        
    }
    # return payload
    payload.update(**kwargs)
    return payload
    
# if __name__ == "__main__":
    # patient_payload()
    
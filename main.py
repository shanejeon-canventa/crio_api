# Main entry point to run application & operations
from crio_sdk import Config,  CrioClient, DonorResource

def donor_payload(first_name, last_name, dob, did, email):
    config = Config()
    return {
        "siteId": "2381",
        "patientInfo": {
            "patientId": "null",
            "externalId": did,
            "birthDate": dob,
            "status": "AVAILABLE", 
            "patientContact": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email
            }
        }
    } 
    
def main():
    config = Config()

    print(f"Connecting to: {config.base_url}")
    print(f"Client ID: {config.client_id}")
    
    client = CrioClient(config)
    donor_api = DonorResource(client)
    
    # print("Fetching donor...")
    # site_id = config.site_id
    # test_donor_id = "2678519"
    # test_donor = donor_api.get_donor_by_id(test_donor_id, site_id)
    # print(f"TEST DONOR: {test_donor}")
    
    test_donor_payload = donor_payload("hillery", "bogace", "02-DEC-1980", "CE0009886", "hillery.bogace@everyma1l.biz")
    print("creating donor...")
    created_donor = donor_api.create_donor(test_donor_payload)  
    print("Created Donor Response", created_donor)
    
    
if __name__ == "__main__":
    main()
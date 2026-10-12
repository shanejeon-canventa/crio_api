# Main entry point to run application & operations
import json
from crio_sdk import Config,  CrioClient, DonorResource, DonorPayload

def import_json_raw_data(json_file):
    with open(json_file, "r") as f:
        raw_data = json.load(f)
        
    donors = DonorPayload.from_list(raw_data)
    return donors
    # for donor in donors:
    #     print(f"Loaded donor: {donor.first_name} {donor.last_name}")
    #     payload = donor.to_dict()
    # return payload

def main():
    config = Config()

    print(f"Connecting to: {config.base_url}")
    print(f"Client ID: {config.client_id}")
    
    client = CrioClient(config)
    donor_api = DonorResource(client)
    
    dummy_data_path = config.get_file_path()
    test_donors = import_json_raw_data(dummy_data_path)
    
    for donor in test_donors:
        # print(f"Loaded donor: {donor.first_name} {donor.last_name}")
        payload = donor.to_dict()
        print(f"!!! PAYLOAD: {payload} !!!")
        donor_api.create_donor(payload)
        
    # print(test_payload)
    # test_data = config.get_file_path()
    
    # print("Fetching donors...")
    # export_data = import_json_export_payload(dummy_data)
    # print(f"\n EXPORT DATA: {export_data}\n")
    # site_id = config.site_id
    # test_donor_id = "2678519" #api test donor
    # test_donor = donor_api.get_donor_by_id(test_donor_id, site_id)
    # print(f"TEST DONOR: {test_donor}")
    
    # sandbox_donor_id = "7819360"
    # sandbox_donor = donor_api.get_donor_by_id(sandbox_donor_id, site_id)
    # print(f"SANDBOX DONOR: {sandbox_donor}")
    
    # # prod_donor_id = "7303778"
    # # prod_donor = donor_api.get_donor_by_id(prod_donor_id, site_id)
    # # print(f"PROD DONOR: {prod_donor}")
    # test_donor_payload = donor_payload("Alameda", "MacDowall", "12-APR-1964", "CE0006362", "alameda.macdowall@gma1l.org")
    # # test_donor_payload1 = donor_payload("Alameda", "MacDowall", "21-APR-2000", "CE0010372", "alameda.macdowall@gma1l.org")
    # # test_donor_payload2 = donor_payload("Linc", "Lidster", "24-JAN-1990", "CE0006999", "linc.lidster@hotma1l.net")
    # # total_payload = [test_donor_payload1, test_donor_payload2]
    # print("creating donor...")
    # # # print("TEST", test_donor_payload)
    # # for donor in total_payload:
    # #     print(f"SUCCESSFULLY CREATED DONOR {donor}")
        
        
    # created_donor = donor_api.create_donor(test_donor_payload)  
    # print("Created Donor Response", created_donor)
    
    
if __name__ == "__main__":
    main()
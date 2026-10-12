# Main entry point to run application & operations
import json
from crio_sdk import Config,  CrioClient, DonorResource, DonorPayload, StudyResource, export_to_json

def import_json_raw_data(json_file):
    with open(json_file, "r") as f:
        raw_data = json.load(f)
        
    donors = DonorPayload.from_list(raw_data)
    return donors


def main():
    config = Config()

    print(f"Connecting to: {config.base_url}")
    print(f"Client ID: {config.client_id}")
    
    client = CrioClient(config)
    donor_api = DonorResource(client)
    study_api = StudyResource(client)
    
    dummy_data_path = config.get_file_path()
    test_donors = import_json_raw_data(dummy_data_path)
    
    site_id = config.site_id
    lp_study_id = config.lp_study_id
    trait_study_id = config.trait_study_id
    
    if config.is_production:
        print("STARTING PRODUCTION ENV")
        print("STUDY ID : ", study_id)
        
        # study_info = study_api.get_study_by_id(study_id)
        # print(study_info)
        # export_to_json(study_info)
        # try:
        #     study_procedure_traits = study_api.get_study_trait(study_id)
        #     export_to_json(study_procedure_traits)
        #     print(study_procedure_traits)
        # except Exception as e:
        #     print(f"error: {e}")
        try:
            print("PROD IS TRUE")
            # trait_study_data = study_api.get_study_by_id(trait_study_id)
            # # print(trait_study_data)
            # export_to_json(trait_study_data, "trait_study_by_id_data.json")
            
            # study_procedure_traits = study_api.get_study_trait(trait_study_id)
            # export_to_json(study_procedure_traits, "study_procedure_traits.json")

            # site_procedure_traits = study_api.get_site_trait()
            # export_to_json(site_procedure_traits, "site_procdure_traits.json")
            # print(site_procedure_traits)
        except Exception as e:
            print(f"error: {e}")
    else:
        # print("!!! TESTING FOR SANDBOX !!!")
        # trait_study_data = study_api.get_study_by_id(trait_study_id)
        # # print(trait_study_data)
        # export_to_json(trait_study_data, "export/trait_study_by_id_data.json")
        
        # study_procedure_traits = study_api.get_study_trait(trait_study_id)
        # export_to_json(study_procedure_traits, "export/study_procedure_traits.json")

        # site_procedure_traits = study_api.get_site_trait()
        # export_to_json(site_procedure_traits, "site_procdure_traits.json")
        # print(site_procedure_traits)
        for donor in test_donors:
            # print(f"Loaded donor: {donor.first_name} {donor.last_name}")
            payload = donor.to_dict()
            # print(f"!!! PAYLOAD: {payload} !!!")
            new_donor = donor_api.create_donor(payload)
            print("!!! NEW DONOR CREATED IN CRIO: ", new_donor, "!!!")
        
        # get_newly_created_donors = 
        # for donor in test_donors:
        #     print(donor)
            
        # print(test_payload)
        # #     donor_api.create_donor(donor)
        # test_data = config.get_file_path()
        
        # test_donor_id = "2679045" #api test donor
        # test_donor_contact = {
        #     # "siteId": config.site_id,
        #     "siteId": site_id,
        #     "email": "ruth.waddingham@everyma1l.co.uk",
        #     "homePhone": "332-332-3323"
        #     # "cellPhone": None
        # }

        # test_get_donor_by_contact = donor_api.get_donor_by_contact(test_donor_contact)
        # print(f"TEST DONOR BY CONTACT: {test_get_donor_by_contact}")
    # elif config.is_production:

    
    
if __name__ == "__main__":
    main()
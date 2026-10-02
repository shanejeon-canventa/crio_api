# Main entry point to run application & operations
import csv
from crio_sdk import Config,  CrioClient, DonorResource
from crio_sdk.config import load_json_data
# from payloads import patient

def main():
    config = Config()

    print(f"Connecting to: {config.base_url}")
    print(f"Client ID: {config.client_id}")
    
    client = CrioClient(config)
    donor_api = DonorResource(client)
    
    mansfield_data = load_json_data()
    # print(f"MANSFIELD DATA: {mansfield_data}")
    def load_csv_dict_reader(csv_path:str):
        with open(csv_path, mode='r', encoding='utf-8-sig') as data:
            reader = csv.DictReader(data)
            return list(reader)
            # return reader
    csv_file_path = mansfield_data.get("mansfield_donors")
    csv_data = load_csv_dict_reader(csv_file_path)
    
    def load_donor_data(donor_data:dict)  -> list:
        parsed_donors = []
        # print(donor_data[0])
        for i, row in enumerate(donor_data, start=1):
            donor_id = row.get("DID", "")
            dob = row.get("DOB (MM/DD/YY)", "")
            sex = row.get("Sex (M/F)", "")
            race = row.get("Race", "")
            ids_expiry = row.get("90 day virals", "")
            return_eligibility = row.get("Return Eligibility", "")
            bmi = row.get("BMI", "")
            
            parsed_donors.append({
                "donor_id": donor_id,
                "dob": "dob",
                "sex": sex,
                "race": race,
                "ids_expiry": ids_expiry,
                "return_date": return_eligibility,
                "bmi": bmi
            })
            
        return parsed_donors
    # print("LOAD DONOR DATA TEST: ", load_donor_data(csv_data))\
    parsed_donors = load_donor_data(csv_data)
    
    def filter_donors(donor_list:list)->list:
        donors_with_race = []
        for donor in donor_list:
            race = donor.get("race", "")
            if race != "":
                donors_with_race.append(donor)
        # for donor in donor_list:
        #     if donor['race'] == "":
        #         print("DONOR RACE:", donor["race"])
        #         continue
        #     else:
        #         donors_with_race.append(donor)
                
        return donors_with_race
    # print(f"TEST FILTERS: ", filter_donors(parsed_donors))    
    active_donors = filter_donors(parsed_donors)
    
    def get_donor_crio_data(donors, site_id):
        req_data = []
        for donor in donors:
            donor_id = donor.get("donor_id")
            if donor_id == "":
                print("NO DONOR ID")
                continue
            search_criteria = {
                "patientId": donor_id
            }
            
            get_donor = donor_api.search_donor(search_criteria)
            matches = get_donor.get("matches", "")
            if len(matches) == 0:
                continue
            # print("GET DONOR: ", get_donor)
            req_data.append({
                "donor_id": donor_id,
                "firstName": matches[0]["firstName"],
                "lastName": matches[0]["lastName"],
                "email": matches[0]["email"]
            })
        return req_data
    
    site_id = config.site_id
    data_for_question_scraping = get_donor_crio_data(active_donors, site_id)    
    print("TEST RETRIEVAL FOR BASIC INFO:", data_for_question_scraping)
        
        
    
    
    # # load_csv_dict_reader(mansfield_data.mansfield_donors)
    # print("Fetching donors...")
    # # search_criteria = {
    # #     # "patientId": "2678519"
    # #     "patientId": "7372663"
    # # }

    
    # search_result =  donor_api.search_donor(search_criteria)
    # print(f"SEARCH RESULT: {search_result}")
    
    
if __name__ == "__main__":
    main()
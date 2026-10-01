# Main entry point to run application & operations
from crio_sdk import Config,  CrioClient, DonorResource


def main():
    config = Config()

    print(f"Connecting to: {config.base_url}")
    print(f"Client ID: {config.client_id}")
    
    client = CrioClient(config)
    donor_api = DonorResource(client)
    
    print("Fetching donor...")
    site_id = config.site_id
    test_donor_id = "2678519"
    test_donor = donor_api.get_donor_by_id(test_donor_id, site_id)
    print(f"TEST DONOR: {test_donor}")
    
    
if __name__ == "__main__":
    main()
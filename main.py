# Main entry point to run application & operations
from crio_client.config import Config
from crio_client.client import CrioClient
from crio_client.resource import PatientResource

def main():
    Config.validate #validates base url, required headers, token, and site id
    
    # instantiating API client and service
    client = CrioAPIClient()
    service = PatientResource(client)
  
    # add new patient method
    # add print statement to confirm new patient has been created
    
    # same with put request ^^^
    
if __name__ == "__main__":
    main()
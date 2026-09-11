# Main entry point to run application & operations
from crio_client.client import CrioAPIClient
from crio_client.services.resource import ResourceService

def main():
    client = CrioAPIClient()
    service = ResourceService(client)
    
    data = service.get_resource("")
    print(f"Data: {data}")
    
if __name__ == "__main__":
    main()
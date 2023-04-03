from requests_ip_rotator import ApiGateway

# Create gateway object and initialise in AWS
gateway = ApiGateway("https://site.com")
gateway.start()

# Assign gateway to session
session = requests.Session()
session.mount("https://site.com", gateway)
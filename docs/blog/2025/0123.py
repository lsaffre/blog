# See https://luc.lino-framework.org/blog/2025/0123.html
from pathlib import Path
import requests
import base64
import sys
import json
import uuid
from pprint import pprint

# Define client ID and secret
client_id = "69d85961-7d68-474d-9ac2-426fdc71bab8"
client_secret = "valid_client_secret"

# Define certificate and key file paths
cert_dir = Path(f"~/Documents/ibanity/application_{client_id}/").expanduser()
cert_file = cert_dir / "certificate.pem"
key_file = cert_dir / "decrypted_private_key.pem"

# Validate if the key and certificate files exist
if not cert_file.exists():
    raise Exception(f"Error: Certificate file not found at {cert_file}")

if not key_file.exists():
    raise Exception(f"Error: Private key file not found at {key_file}")

# Base64 encode client_id and client_secret for Basic Auth
client_credentials = f"{client_id}:{client_secret}"
encoded_credentials = base64.b64encode(client_credentials.encode()).decode()

# Create an HTTPS session
s = requests.Session()

# Attach client certificate and key to the session
s.cert = (cert_file, key_file)

# Add the Authorization header
headers = {
    "Authorization": f"Basic {encoded_credentials}",
    "Content-Type": "application/x-www-form-urlencoded",  # Required for OAuth2 requests
}

url = "https://api.ibanity.com/einvoicing/oauth2/token"
data = {"grant_type": "client_credentials"}
response = s.post(url, data=data, headers=headers)
if response.status_code != 200:
    raise Exception(f"Unexpected response status code: {response.status_code}\n{response.text}")
rv = json.loads(response.text)
access_token = rv['access_token']

# Customer search. Check whether my customer exists.
# Belgian participants are registered with the Belgian company number, for which
# identifier 0208 can be used. Optionally, the customer can be registered with
# their VAT number, for which identifier 9925 can be used.

print("Customer search")
url = "https://api.ibanity.com/einvoicing/peppol/customer-searches"
eas = "9925"
vat_id = "BE0010012671"
# The Flowin sandbox contains hard-coded fake data.  Using another reference as
# customerReference will in result a 404

headers = {
    "Accept": "application/vnd.api+json",
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/vnd.api+json"
}
# pprint(headers)
data = {
    "type": "peppolCustomerSearch",
    # "id": str(uuid.uuid4()),
    "attributes": {
        "customerReference": f"{eas}:{vat_id}",
        # "supportedDocumentFormats": doc_formats
    }
}
data = {"data": data}
# pprint(data)
response = s.post(url, headers=headers, json=data)
if response.status_code != 200:
    msg = f"POST {url} returned {response.status_code}\n{response.text}\n"
    raise Exception(msg)
rv = json.loads(response.text)
pprint(rv)

from pathlib import Path
import requests
import base64
import sys
import json
from pprint import pprint

# Set EXAMPLE to 1 or 2, see https://luc.lino-framework.org/blog/2025/0118.html
EXAMPLE = 2

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
try:
    response = s.post(url, data=data, headers=headers)
except requests.exceptions.SSLError as e:
    raise Exception(f"SSL Error: {e}. Please ensure your certificate and private key are correct and properly configured.")
except requests.exceptions.RequestException as e:
    raise Exception(f"Request Error: {e}")
if response.status_code != 200:
    raise Exception(f"Unexpected response status code: {response.status_code}")
rv = json.loads(response.text)
access_token = rv['access_token']

# Same headers dict used in all examples
headers = {
    "Accept": "application/vnd.api+json",
    "Authorization": f"Bearer {access_token}"
}

# I don't know whether the access token allows multiple requests, so I skip
# this one for example 2.
if EXAMPLE == 1:
    print("Get a list of suppliers")
    url = "https://api.ibanity.com/einvoicing/suppliers"
    response = s.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Unexpected status code {response.status_code} for GET {url}")
    rv = json.loads(response.text)
    pprint(rv)
    sys.exit()

# Customer search. Check whether my customer exists.
# Belgian participants are registered with the Belgian company number, for which
# identifier 0208 can be used. Optionally, the customer can be registered with
# their VAT number, for which identifier 9925 can be used.

if EXAMPLE == 2:
    print("Customer search")
    url = "https://api.ibanity.com/einvoicing/customer-searches"
    eas = "9925"
    vat_id = "BE0010012671"
    # vat_id = "BE0840559537"
    # headers are the same as before, plus a new header "Content-Type"
    headers["Content-Type"] = "application/vnd.api+json"
    # pprint(headers)
    data = {
        "type": "peppolCustomerSearch",
        "attributes": {
          "customerReference": f"{eas}:{vat_id}"
        }
    }
    # data = {"data": data}
    pprint(data)
    response = s.post(url, headers=headers, data=data)
    if response.status_code != 200:
        print(response.text) # line added 20250121
        raise Exception(f"Unexpected status code {response.status_code} for POST {url}")
    rv = json.loads(response.text)
    pprint(rv)

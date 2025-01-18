from pathlib import Path
import requests
import base64
import sys
import json
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
    print(f"Error: Certificate file not found at {cert_file}")
    sys.exit(1)

if not key_file.exists():
    print(f"Error: Private key file not found at {key_file}")
    sys.exit(1)

# Base64 encode client_id and client_secret for Basic Auth
client_credentials = f"{client_id}:{client_secret}"
encoded_credentials = base64.b64encode(client_credentials.encode()).decode()

# Create an HTTPS session
s = requests.Session()

try:
    # Attach client certificate and key to the session
    s.cert = (cert_file, key_file)

    # Add the Authorization header
    headers = {
        "Authorization": f"Basic {encoded_credentials}",
        "Content-Type": "application/x-www-form-urlencoded",  # Required for OAuth2 requests
    }

    # Make the POST request
    response = s.post(
        "https://api.ibanity.com/einvoicing/oauth2/token",
        data={"grant_type": "client_credentials"},
        headers=headers
    )

    # Handle response
    print(f"Response status: {response.status_code}")
    # print(f"Response body: {response.text}")
    rv = json.loads(response.text)
    print("Response text:")
    pprint(rv)

except requests.exceptions.SSLError as ssl_error:
    print(f"SSL Error: {ssl_error}")
    print("Please ensure your certificate and private key are correct and properly configured.")

except requests.exceptions.RequestException as req_error:
    print(f"Request Error: {req_error}")

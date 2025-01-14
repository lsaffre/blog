from pathlib import Path
import requests

client_id = "69d85961-7d68-474d-9ac2-426fdc71bab8"
pth = Path(f"~/.ssh/ibanity/application_{client_id}/")
pth = pth.expanduser()

cert_file = pth / "certificate.pem"
key_file = pth / "decrypted.private_key.pem"

s = requests.Session()
# s.cert = (key_file, cert_file)
s.cert = (cert_file, key_file)

r = s.get("https://api.ibanity.com/einvoicing/suppliers?")
print(r)

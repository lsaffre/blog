import json
import requests
from pprint import pprint
server_url = "https://matrix.org"
url = server_url + "/.well-known/matrix/client"
session = requests.Session()
response = session.get(url)
assert response.status_code in {200, 201, 202, 204, 400}
pprint(json.loads(response.text))

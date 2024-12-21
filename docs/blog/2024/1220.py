import hashlib
from lxml import etree
import urllib.request
import urllib.parse

# copied from sml.py:
# SML: receiver -> domain (DNS)

def get_domain_using_http(receiver, test):
    smp_id = 'B-' + hashlib.md5((receiver.lower()).encode("utf-8")).hexdigest()
    return f'{smp_id}.iso6523-actorid-upis.{get_server(test)}'

def get_server(test):
    if test:
        return 'acc.edelivery.tech.ec.europa.eu'
    else:
        return 'edelivery.tech.ec.europa.eu'

# copied from smp.py:
# SMP: domain + path -> xml with service descriptions

def get_smp_info(domain, receiver):
    # all the available interfaces (invoice, credit note etc.)
    url = 'http://' + domain + "/iso6523-actorid-upis::" + receiver
    print(f"request from url {url}")
    contents = urllib.request.urlopen(url).read()
    print(contents)
    return contents

invoice_end = urllib.parse.quote("billing:3.0::2.1")

def find_invoice_smp_document(smp_contents):
    root = etree.fromstring(smp_contents)
    for child in root:
        for el in child:
            if el.get('href').endswith(invoice_end):
                return el.get('href')

def extract_as4_information(smp_contents):
    invoice_url = find_invoice_smp_document(smp_contents)
    invoice_smp = urllib.request.urlopen(invoice_url).read()
    root = etree.fromstring(invoice_smp)
    #id = root.findall(".//{*}ParticipantIdentifier")[0].text
    as4_endpoint = root.findall(".//{*}EndpointReference")[0][0].text
    certificate = root.findall(".//{*}Certificate")[0].text
    return [as4_endpoint, certificate]


their_id = "9931:EE100588749"  # Rumma & Ko OÜ
test = True

smp_domain = get_domain_using_http(their_id, test)
print(f"smp_domain is {smp_domain}")
smp_contents = get_smp_info(smp_domain, their_id)
url, their_cert = extract_as4_information(smp_contents)
print(url, their_cert)

#their_certfile = '/tmp/their-cert.pem'
#with open(their_certfile, 'w') as f:
#    f.write('-----BEGIN CERTIFICATE-----\n' + their_cert + '\n-----END CERTIFICATE-----')

# usage
import sys
from lino.api.shell import contacts
from lxml import etree
from lino.utils import Cycler

from lino_cosi.lib.sepa.fixtures.sample_ibans import IBANS

PERSONS = Cycler(contacts.Person.objects.exclude(national_id=''))

tree = etree.parse(sys.argv[1])

for e in tree.getroot().getiterator():
    if e.tag.endswith("NationalNumber"):
        e.text = SSIDS.pop()
    if e.tag.endswith("}Nm"):
        e.text = PARTNERS.pop().name

print etree.tostring(tree)

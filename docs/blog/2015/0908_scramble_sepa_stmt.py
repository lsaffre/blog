# usage 
import sys
from lino.api.shell import contacts
from lxml import etree
from lino.utils import Cycler

from lino.modlib.sepa.fixtures.sample_ibans import IBANS

IBANS = Cycler(IBANS)
PARTNERS = Cycler(contacts.Partner.objects.all())

tree = etree.parse(sys.argv[1])

for e in tree.getroot().getiterator():
    if e.tag.endswith("}IBAN"):
        e.text = IBANS.pop()
    if e.tag.endswith("}Nm"):
        e.text = PARTNERS.pop().name

print etree.tostring(tree)

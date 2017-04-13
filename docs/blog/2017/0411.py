from lino import startup
startup('lino_welfare.projects.eupen.settings.demo')
from django.utils import translation
from builtins import str
from lino.api.shell import *

# rt.show(cal.GuestStates)

reason = pcsw.RefusalReasons.get_by_value('20')
# reason = cal.GuestStates.get_by_value('45')
translation.activate('de')
print reason
print repr(str(reason))
print type(str(reason))


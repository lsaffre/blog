from lino import startup

startup('lino_welfare.projects.eupen.settings.demo')

from rstgen import table
from lino.api.shell import *
from lino_welfare.modlib.welfare.roles import *

roles = [
    OfficeOperator, OfficeUser, SepaUser, DebtsUser, LedgerStaff, Supervisor,
    SiteAdmin
]
rows = []
headers = ["Profile"]
for r in roles:
    headers.append(r.__name__)
for p in users.UserTypes.objects():
    row = [p.text]
    for r in roles:
        row.append("X" if p.has_required_roles([r]) else "")
    rows.append(row)

print(table(headers, rows))

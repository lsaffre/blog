# -*- coding: UTF-8 -*-
from __future__ import print_function
import csv
import os

ignored_views = set(["HHB", "FFO", "FFOI"])
seen_views = set([])
seen_aliases = set([])
seen_groups = set([])
tpl = "check_journal(u'{1}', u'{4}', u'{11}', u'{10}')"

print("""# -*- coding: UTF-8 -*-
from __future__ import print_function
from lino.api import rt

ledger = rt.models.ledger
finan = rt.models.finan
vatless = rt.models.vatless


def check_journal(ref, name, view, group):
    if ledger.Journal.objects.filter(ref=ref).count():
        print("Journal", ref, "exists")
        return
    if not group:
        return
    if view == "REG":
        voucher_type = 'vatless.ProjectInvoicesByJournal'
    elif view == "AAW":
        voucher_type = 'finan.DisbursementOrdersByJournal'
    elif view == "KAS":
        voucher_type = 'finan.BankStatementsByJournal'
    elif view == "ZAU":
        voucher_type = 'finan.PaymentOrdersByJournal'
    else:
        return
    grp = ledger.JournalGroups.get_by_name(group.lower())
    obj = ledger.Journal(ref=ref, name=name, voucher_type=voucher_type,
                         journal_group=grp)
    obj.full_clean()
    # uncomment the following line when ready:
    # obj.save()
    print("Journal", ref, "has been created")

""")

with open(os.path.expanduser('~/Downloads/JNL.csv'), 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for row in reader:
        row = [x.strip() for x in row]
        alias = row[2].strip()
        group = row[10].strip()
        view = row[11].strip()
        if alias in ["IMP"]:
            if view not in ignored_views:
                seen_views.add(view)
                seen_aliases.add(alias)
                seen_groups.add(group)
                print(tpl.format(*row))
                # print(', '.join(row))


#print("# Seen aliases:", seen_aliases)
print("# Seen views:", seen_views)
print("# Seen groups:", seen_groups)


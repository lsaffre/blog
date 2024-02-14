# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function
from lino.api.shell import *
from clint.textui import puts, prompt, progress
from lino.core.utils import PseudoRequest
from lino.core.diff import ChangeWatcher

# rt.show(pcsw.ClientStates)
# rt.show(changes.Changes)

former = pcsw.ClientStates.former
# refused = pcsw.ClientStates.refused

qs = pcsw.Coaching.objects.filter(client__client_state=former,
                                  end_date__isnull=True)
# qs = pcsw.Coaching.objects.filter(client__client_state=former)

puts("{0} unbeendete Begleitungen ehemaliger Klienten".format(qs.count()))

clients = dict()
for o in progress.dots(qs):
    lst = clients.setdefault(o.client.id, [])
    lst.append(o)

puts("{0} Klienten".format(len(clients)))
puts("Davon Klienten mit mehr als einer Begleitung:")
for lst in clients.values():
    if len(lst) != 1:
        print("- {0} : {1}".format(lst[0].client, [o.user for o in lst]))

ok = prompt.query("Ready to go?", default="n")

if ok.upper() == "Y":

    REQUEST = PseudoRequest("robin")

    for obj in progress.dots(qs):
        cw = ChangeWatcher(obj)
        obj.end_date = obj.client.modified.date()
        obj.full_clean()
        obj.save()
        cw.send_update(REQUEST)

# rt.show(changes.Changes)

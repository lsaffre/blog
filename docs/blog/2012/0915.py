from lino_welfare.modlib.pcsw import models as pcsw
from lino.api import dd, rt
pcsw = dd.resolve_app('pcsw')
users = dd.resolve_app('users')
root = users.User.objects.get(username='root')
print pcsw.UsersWithClients.request(user=root).to_rst()


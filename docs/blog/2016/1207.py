# -*- coding: UTF-8 -*-
# #1300 (py2js() and dict with newstr)

from builtins import str
from future.types import newstr
import six

items = [str('c'), u'ä2', 'b', 'd', 'a1']
def sortkey(x):
    if isinstance(x, newstr):
        return six.text_type(x)
    return x
# items = sorted(items, key=sortkey)
try:
    items = sorted(items, key=sortkey)
except TypeError as e:
    raise TypeError("Failed to sort {0} : {1}".format(items, e))
print items

print isinstance(str('a'), newstr)

print isinstance(u'a', newstr)


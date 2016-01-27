# -*- coding: utf-8 -*-
import sys, codecs
# from io import StringIO
from cStringIO import StringIO
buffer = StringIO()

wrapper = codecs.getwriter("utf8")(buffer)
old = sys.stdout
sys.stdout = wrapper
print(u"Palju õnne")
sys.stdout = old
print buffer.getvalue()

import sys
from io import StringIO
old = sys.stdout
buffer = StringIO()
sys.stdout = buffer
print("Foo")
sys.stdout = old
print buffer.getvalue()

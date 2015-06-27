
class A(object):
    pass


class B(object):
    pass

b = B()

print isinstance(b, (A, B))

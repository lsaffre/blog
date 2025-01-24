class A:

    @classmethod
    def meth(cls):
        print("A")

class B(A):

    @classmethod
    def meth(cls):
        super().meth()
        print("B")

class C(A):

    @classmethod
    def meth(cls):
        super().meth()
        print("C")

class D(B, C):

    @classmethod
    def meth(cls):
        super().meth()
        print("D")

D.meth()

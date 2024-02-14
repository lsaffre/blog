from __future__ import print_function


class DummyField(object):

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return None


class Layout(object):
    pass


class DefaultPartnerDetail(Layout):
    main = "a"
    a = DummyField()


class PartnerDetailMixin(Layout):
    if False:
        b = DummyField()
    else:
        b = DummyField()


class MyPartnerDetail(DefaultPartnerDetail, PartnerDetailMixin):
    main = "a b"


dtl = MyPartnerDetail()
for k in dtl.main.split():
    print(k, getattr(dtl, k, "undefined"))

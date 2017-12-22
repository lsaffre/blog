from lino import startup
startup('lino_book.projects.team.settings.demo')
from lino.api.doctest import *
# from django.forms
# from django.forms import ModelForm
# from django import forms
from django.forms import modelform_factory

frm_class = modelform_factory(
    model=rt.models.contacts.Person)
    # fields=["first_name", "last_name"])


p = rt.models.contacts.Person.objects.all()[0]
values = {}
frm = frm_class(p)
frm.as_p()

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'lino_book.projects.max.settings.doctests'
import django
django.setup()
import lino_voga.lib.voga.user_types
import lino_vilma.lib.vilma.user_types


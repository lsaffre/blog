from __future__ import print_function
from django.conf import settings
from django.core.mail import EmailMessage
for k in """EMAIL_HOST EMAIL_HOST_USER
 DEFAULT_FROM_EMAIL SERVER_EMAIL EMAIL_PORT EMAIL_USE_TLS
 """.split():
    print("{0} : {1}".format(k, getattr(settings, k)))

email = EmailMessage('Subject', 'Body', to=['luc.saffre@gmx.net'])
email.send()

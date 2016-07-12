.. _admin.smtp:

=============================
Setting up my own SMTP server
=============================

These are just my personal notes. No warranty whatsoever.

.. contents:: Table of contents
    :local:
    :depth: 1

Why
===

Might become necessary because OVH don't offer SMTP service to their
cloud servers.


Questions:
    
- Should I change `inet_interfaces
  <http://www.postfix.org/postconf.5.html#inet_interfaces>`__ in my
  :xfile:`main.cf` from `all` to `localhost` or `loopback-only`?

Sources:

- `How To Install and Configure Postfix as a Send-Only SMTP Server on
  Ubuntu 14.04
  <https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-postfix-as-a-send-only-smtp-server-on-ubuntu-14-04>`_

- `SPF kirje <https://help.zone.eu/Knowledgebase/Article/View/55/11/spf-kirje>`_

- `Sender Policy Framework - SPF Record Syntax
  <http://www.openspf.org/SPF_Record_Syntax>`__


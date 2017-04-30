========
About me
========

.. image:: photo.jpg
   :width: 200 px
   :align: right


.. py2rst::
   
    import datetime
    print("""
    My name is **Luc Saffre** (French: `lyk 'safʁə
    <https://en.wikipedia.org/wiki/International_Phonetic_Alphabet>`__).
    I am {} years old and
    work as CEO and senior developer at `Rumma
    & Ko OÜ <http://www.saffre-rumma.net/>`_ where we provide development,
    maintenance and customer support of `free
    <https://en.wikipedia.org/wiki/Free_software>`__ customized database
    applications, mainly using the `Lino framework
    <http://www.lino-framework.org/>`__ of which I am the author.
    """.format(datetime.date.today().year-1968))
   

I was born and grew up in `Eupen
<http://en.wikipedia.org/wiki/Eupen>`_, Belgium.  At the age of 30 I
met an Estonian woman, we married, I moved to Estonia and plan to die
there (not too soon, though).  We have 2 daughters and live in a small
village.


.. toctree::
   :maxdepth: 2

   contact
   cv
   historic

   
.. toctree::
   :maxdepth: 1
   :hidden:

   friends
   sites
   jargon
   /topics/index
   christian

# -*- coding: utf-8 -*-
import lino
from lino.sphinxcontrib import configure

# extlinks = {}
# extensions = []
# templates_path = []

configure(globals(), 'lino_book.projects.min9.settings')

from atelier.sphinxconf import interproject
interproject.configure(globals())
intersphinx_mapping['cg'] = ('https://community.lino-framework.org/', None)
intersphinx_mapping['hg'] = ('https://hosting.lino-framework.org/', None)
intersphinx_mapping['hw'] = ('https://hw.saffre-rumma.net/', None)

extensions += ['atelier.sphinxconf.blog']
extensions += ['atelier.sphinxconf.complex_tables']
extensions += ['lino.sphinxcontrib.logo']
extensions += ['lino.sphinxcontrib.base']  # for tcname
# extensions += ['sphinxcontrib.taglist']
# extensions += ['sphinxcontrib.youtube']
extensions += ['sphinx.ext.inheritance_diagram']

extensions += ['atelier.sphinxconf.sigal_image']

sigal_base_url = 'https://sigal.saffre-rumma.net'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# General substitutions.
project = "Luc's developer blog"
copyright = '2001-2021 Luc Saffre'


html_title = "Luc's dblog"
html_short_title = "Home"
html_logo = "logo2.jpg"

# extlinks.update(ticket=('http://trac.lino-framework.org/ticket/%s', '#'))
# extlinks.update(ticket=('javascript:alert("Sorry, linking to tickets (%s) is not yet implemented!")', '#'))
# extlinks.update(ticket=('https://jane.mylino.net/#/api/tickets/AllTickets/%s', '#'))
extlinks.update(ticket=('https://jane.mylino.net/#/api/tickets/AllTickets/%s', '#'))
extlinks.update({
    'issue': (
        'http://code.google.com/p/lino/issues/detail?id=%s', '# '),
    'checkin': (
        'http://code.google.com/p/lino/source/detail?r=%s', 'Checkin '),
    'srcref': ('https://github.com/lsaffre/blog/blob/master/%s', ''),
    'linosrcref': ('https://github.com/lsaffre/lino/blob/master/%s', ''),
    'extjs': ('http://www.sencha.com/deploy/dev/docs/?class=%s', ''),
    'extux': ('http://extjs-ux.org/ext-docs/?class=%s', ''),
    'djangoticket': (
        'http://code.djangoproject.com/ticket/%s', 'Django ticket #'),
    'welfare': ('https://welfare.lino-framework.org%s.html', ''),
    'lino': ('https://www.lino-framework.org%s.html', ''),
    # 'welfareticket': (
    #     'https://welfare.lino-framework.org/tickets/%s.html', ''),
    # 'welfareusermande': (
    #     'https://welfare-userman.lino-framework.org/de%s.html', ''),
    # 'welfareusermanfr': (
    #     'https://welfare-userman.lino-framework.org/fr%s.html', ''),
})



blogref_format = "https://luc.lino-framework.org/blog/%Y/%m%d.html"


inheritance_graph_attrs = dict(rankdir="TB")
# inheritance_graph_attrs.update(size='"12.0, 16.0"')
inheritance_graph_attrs.update(size='"48.0, 64.0"')
inheritance_graph_attrs.update(fontsize=14, ratio='compress')


# extensions += ['yasfb']
# extensions += ['sphinxcontrib.feed']
extensions += ['sphinxfeed']
# NB : not the public sphinxfeed but my extended version
feed_base_url = 'https://luc.lino-framework.org'
feed_author = 'Luc Saffre'
feed_title = "Luc's developer blog"
feed_field_name = 'date'
feed_description = "Luc's developer blog"

# extensions += ['hieroglyph']  # Generate HTML presentations
# autoslides = False
# slide_numbers = True

import os
os.environ['LC_TIME'] = 'en_GB.UTF-8'

# html_context.update(public_url='https://luc.lino-framework.org')

linkcheck_anchors = False
linkcheck_ignore = [r'http://localhost:\d+/']

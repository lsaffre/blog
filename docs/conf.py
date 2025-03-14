# -*- coding: utf-8 -*-
# fmt: off

from atelier.sphinxconf import configure; configure(globals())

import lino

from lino.sphinxcontrib import configure
configure(globals(), 'lino_book.projects.min9.settings')

intersphinx_mapping.pop("welfare")

# 20240920 Sphinx 8 complains about duplicate entry for welfare. The blog needs
# all three languages of the welfare docs, these are added because
# "lino_welfare" is in the string below.


spec = """getlino lino_amici
lino_presto lino_voga lino_tera lino_welfare lino_shop
lino_avanti lino_react eidreader lino_prima"""  # atelier etgen

from rstgen.sphinxconf import interproject; interproject.configure(globals(), spec)

# intersphinx_mapping['book'] = ('https://dev.lino-framework.org/', None)
# intersphinx_mapping['lf'] = ('https://www.lino-framework.org/', None)
# intersphinx_mapping['cg'] = ('https://community.lino-framework.org/', None)
intersphinx_mapping['hg'] = ('https://hosting.lino-framework.org/', None)

intersphinx_mapping['hw'] = ('https://hw.saffre-rumma.net/', None)
intersphinx_mapping['ug_dedocs'] = ('https://using.lino-framework.org/de/', None)
intersphinx_mapping['www'] = ('https://www.saffre-rumma.net/', None)
intersphinx_mapping['ttdocs'] = ('https://timtools.lino-framework.org/', None)

extensions += ['rstgen.sphinxconf.blog']
extensions += ['rstgen.sphinxconf.complex_tables']
extensions += ['lino.sphinxcontrib.logo']
extensions += ['lino.sphinxcontrib.base']  # for tcname
# extensions += ['sphinxcontrib.taglist']
# extensions += ['sphinxcontrib.youtube']
extensions += ['sphinx.ext.inheritance_diagram']

extensions += ['rstgen.sphinxconf.sigal_image']

sigal_base_url = 'https://sigal.saffre-rumma.net'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# General substitutions.
project = "Luc's developer blog"
import datetime

copyright = '2001-{} Luc Saffre'.format(datetime.date.today().year)

html_title = project
html_short_title = "Home"
html_logo = "logo2.jpg"

# extlinks.update(ticket=('http://trac.lino-framework.org/ticket/%s', '#'))
# extlinks.update(ticket=('javascript:alert("Sorry, linking to tickets (%s) is not yet implemented!")', '#'))
# extlinks.update(ticket=('https://jane.mylino.net/#/api/tickets/AllTickets/%s', '#'))
extlinks.update(ticket=('https://jane.mylino.net/#/api/tickets/AllTickets/%s',
                        '#%s'))
extlinks.update({
    # 'issue': ('http://code.google.com/p/lino/issues/detail?id=%s', '#%s'),
    'checkin': ('http://code.google.com/p/lino/source/detail?r=%s', None),
    'srcref': ('https://github.com/lsaffre/blog/blob/master/%s', '%s'),
    'linosrcref':
    ('https://gitlab.com/lino-framework/lino/blob/master/%s', '%s'),
    'extjs': ('http://www.sencha.com/deploy/dev/docs/?class=%s', None),
    'extux': ('http://extjs-ux.org/ext-docs/?class=%s', None),
    'djangoticket':
    ('http://code.djangoproject.com/ticket/%s', 'Django ticket #%s'),
    'welfare': ('https://welfare.lino-framework.org%s.html', None),
    'lino': ('https://www.lino-framework.org%s.html', None),
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
feed_title = project
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

templates_path.append(".templates")

# rst_prolog = """
# :doc:`Blog </blog/2023/index>`
# :doc:`/about/index`
#
# """

html_use_index = True

#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jean-Luc Stevens'
SITENAME = u'Cortical Code'
SITEURL = 'http://jlstevens.github.io/cortical-code'
TIMEZONE = 'Europe/London'
DEFAULT_LANG = u'en'
PATH = 'content'


THEME='./pelican-mockingbird' # pelican-alchemy was considered

PLUGIN_PATHS = ['./pelican-plugins'] # Clone of the repository
PLUGINS = ['summary',                # Allows breaks
           'liquid_tags.youtube',    # May be useful e.g: {% youtube lEEa83Tsjrg %}
           'liquid_tags.notebook']   # Useful!

NOTEBOOK_DIR = 'notebooks'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

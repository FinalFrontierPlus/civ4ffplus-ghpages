# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'TC01 and God-Emperor'
SITENAME = u'Final Frontier Plus'
SITEURL = ''

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Civfanatics Forum', 'http://forums.civfanatics.com/forumdisplay.php?f=387'),
          ('ModDB Page', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('CivFanatics', 'http://forums.civfanatics.com/forumdisplay.php?f=387'),
          ('Github', 'https://github.com/FinalFrontierPlus/'),
          ('ModDB Page', 'http://www.moddb.com/mods/final-frontier-plus'))

STATIC_PATHS = ['extras']

# Don't clutter the toplevel directory
ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{slug}.html'

# Favicon!
EXTRA_PATH_METADATA = {
	'extras/favicon.ico': {'path': 'favicon.ico'},
}

DEFAULT_PAGINATION = 10

THEME = "themes/bootstrap-ffplus"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

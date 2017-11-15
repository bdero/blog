#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'bdero'
SITENAME = "bran's blog"
SITEURL = 'http://blog.bdero.me'

PATH = 'content'

TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

PLUGIN_PATHS = ['plugins']

# Social widget

SOCIAL = (
    ('GitHub', 'https://github.com/bdero'),
    ('Keybase', 'https://keybase.io/bdero'),
    ('LinkedIn', 'https://www.linkedin.com/in/bderosier/'),
    ('Twitter', 'https://twitter.com/cheesekeg'),
)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Theme configuration

THEME = 'themes/attila'
HEADER_COVER = 'images/banner1500x500.jpeg'
HEADER_COLOR = 'black'

AUTHORS_BIO = {
    "bdero": {
        "name": "Brandon DeRosier",
        "cover": "images/banner1500x500.jpeg",
        "image": "images/avatar.jpg",
        "website": "https://blog.bdero.me",
        "location": "Boston, MA",
        "bio": "This is the place for a small biography with max 200 characters. Well, now 100 are left. Cool, hugh?"
    }
}
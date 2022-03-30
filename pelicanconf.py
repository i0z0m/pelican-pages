#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'i0z0m'
SITENAME = "イズム"
SITEURL = 'https://i0z0m.github.io'

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'
DEFAULT_LANG = 'ja'

GITHUB_URL = "http://github.com/i0z0m/"

DEFAULT_PAGINATION = 10

THEME = "pelican-hss-theme"
SHOW_SOCIAL_SHARE_BUTTON = False
USER_LOGO_URL = SITEURL + '/images/logo.png'
FAVICON = 'favicon.ico'
STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

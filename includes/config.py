#!/usr/bin/env python

import os
from google.appengine.api import app_identity
import includes.exceptions

version = os.environ['CURRENT_VERSION_ID']

facebook_locale = 'en_US'
facebook_app_id = None
facebook_app_secret = None
google_analytics_id = None
google_universal_analytics_id = None


host = '%s.appspot.com' % app_identity.get_application_id()
base_url = 'http://%s' % host

is_devenv = False

#error_email = 'errors@example.com'
#error_email = 'Boilderplate Errors <errors@example.com>'
error_email = None

if os.environ['SERVER_SOFTWARE'].startswith('Development'):
    is_devenv = True

    host = 'localhost:8080'
    base_url = 'http://%s' % host

    facebook_app_id = None
    facebook_app_secret = None
    google_analytics_id = None

    error_email = None

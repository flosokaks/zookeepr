import sys

from wsgiref.handlers import CGIHandler
from pyramid.paster import get_app
import os
application = get_app(
  os.path.normpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'development.ini')), 'main')
CGIHandler().run(application)

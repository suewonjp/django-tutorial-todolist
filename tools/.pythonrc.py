import os, sys, importlib
from django.test.utils import setup_test_environment

setup_test_environment()

prj = importlib.__import__(os.environ['DJANGO_SETTINGS_MODULE'].split('.')[0], fromlist=('settings',))
settings = prj.settings

app_names = [ app.split('.')[0] for app in settings.INSTALLED_APPS if not app.startswith('django') ]
apps = {}
for app in app_names:
    apps[app] = importlib.__import__(app)

### The code so far is general and reusable.
### Add project specific code from here.
from todos.models import Todo
from todos.models import Category


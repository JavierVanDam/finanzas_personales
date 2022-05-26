import os
import django
from datetime import datetime, timedelta, date
from json import dumps
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
print(os.environ.get("DJANGO_SETTINGS_MODULE"))
django.setup()

from django.contrib.sessions.models import Session

# from cuentas.models import Cuenta
# c = Cuenta()

sess = Session.objects.all() #  get(pk='a92d67e44a9b92d7dafca67e507985c0')
print(sess[3].session_data)
print(sess[66].get_decoded())
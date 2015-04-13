import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'voxpopproj.settings')

import django

django.setup()

from voxpop.models import Firm, Review

Firm.objects.all().delete()

Review.objects.all().delete()
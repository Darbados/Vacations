import pytz
from django.conf import settings
from django.utils import timezone


TZ = pytz.timezone(settings.TIME_ZONE)


def store_today():
    return timezone.now().astimezone(TZ).date()

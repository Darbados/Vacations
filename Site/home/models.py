from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from Site.mixins import TimestampMixin


class VacationsUser(AbstractBaseUser, TimestampMixin):
    email = models.EmailField(unique=True)

    is_staff = models.BooleanField(default=False)
    activated_at = models.DateTimeField(null=True)
    subscribed_at = models.DateTimeField(null=True)
    is_approver = models.BooleanField(default=False)
    is_rejector = models.BooleanField(default=False)

    def __str__(self):
        return self.email

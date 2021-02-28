from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from Core.mixins import TimestampMixin
from Core.utils import store_today


class Employee(AbstractBaseUser, TimestampMixin):
    email = models.EmailField(unique=True)

    activated_at = models.DateTimeField()
    deactivated_at = models.DateTimeField(null=True)
    # Admin Employee should be marked as superuser
    is_superuser = models.BooleanField(default=False)
    # If true employee can approve other employee vacations
    is_approver = models.BooleanField(default=False)
    # If true employee can reject other employee vacations
    is_rejector = models.BooleanField(default=False)

    def __str__(self):
        return self.email

    @property
    def is_in_vacation(self):
        today = store_today()
        return self.vacations.filter(
            start_date__lte=today,
            end_date__gte=today,
        ).exists()

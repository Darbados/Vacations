from django.db import models
from django.utils.translation import ugettext_lazy as _

from home.models import VacationsUser


class Vacation(models.Model):
    REASON_PAID_VACATION = 1
    REASON_UNPAID_VACATION = 2
    REASON_ILL_VACATION = 3
    REASON_MATERNITY_VACATION = 4
    REASON_CHOICES = (
        (REASON_PAID_VACATION, _('Paid vacation')),
        (REASON_UNPAID_VACATION, _('Unpaid vacation')),
        (REASON_ILL_VACATION, _('Illness vacation')),
        (REASON_MATERNITY_VACATION, _('Maternity vacation')),
    )

    REJECTION_REASON_NOT_ENOUGH_WORKING_PERIOD = 1
    REJECTION_REASON_NOT_ENOUGH_HUMAN_CAPACITY = 2
    REJECTION_REASON_TOO_LATE_REQUESTED = 3
    REJECTION_REASON_ADMIN_DECISION = 4

    REJECTION_REASON_CHOICES = (
        (REJECTION_REASON_NOT_ENOUGH_WORKING_PERIOD, _('Not enough work experience')),
        (REJECTION_REASON_NOT_ENOUGH_HUMAN_CAPACITY, _('Not enough men left to work')),
        (REJECTION_REASON_TOO_LATE_REQUESTED, _('Too late requested')),
        (REJECTION_REASON_ADMIN_DECISION, _('Admin decided to reject')),
    )

    user = models.ForeignKey(VacationsUser, on_delete=models.PROTECT, related_name='vacations')
    reason = models.IntegerField(choices=REASON_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    confirmed_by = models.ForeignKey(
        VacationsUser,
        on_delete=models.SET_NULL,
        related_name='confirmed_vacations',
        limit_choices_to={'is_approver': True},
        null=True,
    )
    confirmed_at = models.DateTimeField(null=True)
    rejected_by = models.ForeignKey(
        VacationsUser,
        on_delete=models.SET_NULL,
        related_name='rejected_vacations',
        limit_choices_to={'is_rejector': True},
        null=True,
    )
    rejection_reason = models.IntegerField(choices=REASON_CHOICES, null=True)

    def __str__(self):
        return self.reason

    @property
    def display_reason(self):
        return dict(self.REASON_CHOICES)[self.reason]

    @property
    def display_rejection_reason(self):
        return dict(self.REJECTION_REASON_CHOICES)[self.rejection_reason]

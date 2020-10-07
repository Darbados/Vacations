from django.db import models


class Vacation(models.Model):
    reason = models.CharField(max_length=255)

    def __str__(self):
        return self.reason

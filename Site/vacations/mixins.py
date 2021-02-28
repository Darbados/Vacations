from django.db import models


class DescriptionMixin(models.Model):
    description = models.TextField()

    def __str__(self):
        return self.description

    class Meta:
        abstract = True

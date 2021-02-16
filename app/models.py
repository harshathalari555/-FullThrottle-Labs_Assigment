
import pytz
from django.db import models
from timezone_field import TimeZoneField
from django.utils import timezone


class ActivityPeriod(models.Model):
    start_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    end_time = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        """Meta."""
        ordering = ["-id"]

class Member(models.Model):
    id = models.CharField(max_length=10, blank=True,primary_key=True)
    real_name = models.CharField(max_length=50, blank=True, null=True)
    tz = TimeZoneField(default='America/Los_Angeles')
    activity_periods = models.ManyToManyField(ActivityPeriod, related_name='activity_periods', null=True, blank=True)


    def __str__(self):
        """__str__."""
        return self.real_name

    class Meta:
        """Meta."""
        ordering = ["-id"]


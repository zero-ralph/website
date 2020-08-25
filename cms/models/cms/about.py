from ..base_imports import *


class About(models.Model):
    subtitle = models.CharField(max_length=255, null=True, blank=True)
    position_header = models.CharField(max_length=255, null=True, blank=True)
    position_sub_header = models.CharField(max_length=255, null=True, blank=True)
    freelance = models.BooleanField(default=True)
    location = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'about'
    
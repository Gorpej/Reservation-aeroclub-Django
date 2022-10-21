
from django.db import models

# Create your models here.


class Slot(models.Model):
    date = models.DateField(blank=True)
    start_times = models.IntegerField(blank=True)
    end_times = models.IntegerField(blank=True)
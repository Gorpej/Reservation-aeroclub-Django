from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=70)
    first_name = models.CharField(max_length=70)
    email = models.EmailField()
    num_aero = models.IntegerField()
    admin = models.BooleanField(default=False)
    avatar = models.ImageField()
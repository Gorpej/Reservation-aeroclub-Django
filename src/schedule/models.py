from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=70)
    first_name = models.CharField(max_length=70)
    email = models.EmailField(max_length=254,unique=True)
    num_aero = models.IntegerField(default=0)
    admin = models.BooleanField(default=False)
    #avatar = models.ImageField()
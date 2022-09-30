from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Vous devez entrer un email")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        user = self.create.user(email=email, password=password)
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user


class CustomUser(AbstractBaseUser):
    name = models.CharField(max_length=70, blank=False)
    first_name = models.CharField(max_length=70, blank=False)
    avatar = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, blank=True)
    email = models.EmailField(max_length=255, unique=True,blank =False)
    num_aero = models.CharField(blank=True, max_length=5)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ["name", "first_name"]

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

"""
class Users(models.Model):
    name = models.CharField(max_length=70)
    first_name = models.CharField(max_length=70)
    email = models.EmailField(max_length=254,unique=True)
    num_aero = models.IntegerField(default=0)
    admin = models.BooleanField(default=False)
    #avatar = models.ImageField()"""
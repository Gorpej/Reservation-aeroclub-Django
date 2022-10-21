from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models


# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email, name, first_name, password=None):
        if not email:
            raise ValueError("Vous devez entrer un email")
        user = self.model(email=self.normalize_email(email),
                          name=name,
                          first_name=first_name)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, name, first_name, password=None):
        user = self.create_user(email=email, password=password, name=name, first_name=first_name)
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user

class CustomUser(AbstractBaseUser):
    name = models.CharField(max_length=70, blank=False)
    first_name = models.CharField(max_length=70, blank=False)
    avatar = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, blank=True)
    email = models.EmailField(max_length=255, unique=True,blank =False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "first_name"]

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
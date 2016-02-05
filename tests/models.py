from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from .managers import UserManager


MALE = "M"
FEMALE = "F"
OTHER = "O"

GENDERS = (
    (MALE, "Male"),
    (FEMALE, "Female"),
    (OTHER, "Other")
)


class User(AbstractBaseUser):

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")
    gender = models.CharField(max_length=1, choices=GENDERS, default="")
    created = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    def get_full_name(self):
        if self.first_name and self.last_name:
            return "{0} {1}".format(self.first_name, self.last_name)
        return self.get_short_name()

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

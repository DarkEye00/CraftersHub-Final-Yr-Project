from django.db import models
from django.contrib.auth.models import AbstractUser, Group


# Create your models here.
class User(AbstractUser):
    """Creating a user in the model."""

    CUSTOMER = "customer"
    VENDOR = "vendor"

    ROLE_CHOICES = [(CUSTOMER, "Customer"), (VENDOR, "Vendor")]

    email = models.EmailField(unique=True, null=False)
    username = models.CharField(max_length=100)
    bio = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=CUSTOMER)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return str(self.username)

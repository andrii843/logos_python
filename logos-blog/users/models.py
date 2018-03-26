from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    street = models.CharField(
        max_length=255,
        verbose_name='Street'
    )

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom User model for Tracademix.
    Extends standard Django user capabilities for future role-based access control.
    """

    pass
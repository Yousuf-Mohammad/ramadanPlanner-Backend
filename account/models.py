from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from account.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    A class implementing a fully featured User model with
    admin-compliant permissions.

    Email and password are required. Other fields are optional.
    """

    email = models.EmailField(_("email address"), unique=True, null=False)
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(
        _("last name"), max_length=150, null=True, blank=True
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext as _


class Account(AbstractUser):
    """
    Customize model of Django `AbstractUser`

    Inherits the following attributes: AbstracBaseUser
        * first_name
        * last_name
        * username
        * password
        * email
        * is_active
        * is_staff
        * last_login

    Inherits the following attributes: PermissionsMixin
        * is_superuser
        * groups
        * user_permissions
    """

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

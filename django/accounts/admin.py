from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts import models


@admin.register(models.Account)
class AccountAdmin(UserAdmin):
    pass

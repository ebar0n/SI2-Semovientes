from accounts import models
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


@admin.register(models.Account)
class AccountAdmin(UserAdmin):
    pass

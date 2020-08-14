from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User as CustomUser
from .models import Privacy


# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser


class PrivacyAdmin(admin.ModelAdmin):
    model = Privacy


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Privacy, PrivacyAdmin)

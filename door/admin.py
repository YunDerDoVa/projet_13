from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User as CustomUser
from .models import Privacy


# Register your models here.
class CustomUserAdmin(UserAdmin):
    """ It is the UserAdmin model to administrate AbstractUser model. """

    model = CustomUser


class PrivacyAdmin(admin.ModelAdmin):
    """ We want to administrate Privacy. """

    model = Privacy


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Privacy, PrivacyAdmin)

from django.contrib import admin
from django.utils.translation import gettext as _

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . import models


class UserAdmin(BaseUserAdmin):
    ordering = ["id"]
    list_display = ["email", "name"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("name",)}),
        (
            _("Permissions"), {
                "fields": ("is_active", "is_staff", "is_superuser", "access")}
        ),
        (_("importent_date"), {"fields": ("last_login", )})
    )

    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": (
            "email", "password1", "password2")}),
    )


admin.site.register(models.User, UserAdmin)

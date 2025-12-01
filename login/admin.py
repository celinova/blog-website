from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm
from .models import UserModel


# change subclass later
class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    model = UserModel
    list_display = [
        "email",
        "username",
        "age",
        "name",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("age",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("age",)}),)


admin.site.register(UserModel, CustomUserAdmin)

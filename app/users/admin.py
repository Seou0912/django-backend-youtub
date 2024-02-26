from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        ("유저정보", {"fields": ("email", "nickname", "password")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
    )

    # 유저를 만들 때 보이는 화면
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "nickname",
                    "is_business",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
    # 보이는 부분
    list_display = ("email", "nickname", "is_business", "is_active", "is_staff")
    search_fields = ("email", "nickname")
    ordering = ("email",)

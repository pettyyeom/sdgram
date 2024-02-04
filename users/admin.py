from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from users.models import User
# Register your models here.

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = [
        (None, {'fields': ('username', 'password')}),
        ("개인정보", {'fields': ('firstname', 'lastname', 'email')}),
        ("추가필드", {'fields': ('profile_image', 'short_description')}),
        (
            "권한",
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            },
        ),
        ("중요한 일정", {'fields': ('last_login', 'date_joined')}),
    ]

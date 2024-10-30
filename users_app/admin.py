from django.contrib import admin
from .models import Users, UserProfile


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'email', 'password', 'role', 'created_at', 'updated_at')


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'gender', 'contact_number', 'address', 'user_id')

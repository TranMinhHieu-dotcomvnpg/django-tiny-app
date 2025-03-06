from django.contrib import admin
from .models import Task
from django.contrib import admin
from django.contrib.auth.models import User

@admin.action(description="Khóa tài khoản đã chọn")
def block_users(modeladmin, request, queryset):
    queryset.update(is_active=False)

@admin.action(description="Mở khóa tài khoản đã chọn")
def unblock_users(modeladmin, request, queryset):
    queryset.update(is_active=True)

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('is_active', 'is_staff')
    actions = [block_users, unblock_users]  # Thêm action vào Admin

# Đăng ký lại model User
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# đăng kí các task
admin.site.register(Task)

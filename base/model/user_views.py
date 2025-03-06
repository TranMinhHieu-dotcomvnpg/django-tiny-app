from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages

def check_user_blocked(user):
    if user.is_authenticated and user.is_blocked:
        messages.error(user, "Tài khoản của bạn đã bị khóa.")
        logout(user)
        return redirect('login')

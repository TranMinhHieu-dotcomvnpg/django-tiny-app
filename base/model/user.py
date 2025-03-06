from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_blocked = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.is_blocked:
            self.is_active = False  # Nếu bị block thì user không thể đăng nhập
        super().save(*args, **kwargs)

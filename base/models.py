from django.db import models
from django.contrib.auth.models import User

class UserMessage(models.Model):
    user_name = models.CharField(max_length=200, null=False, blank=False)
    user_email = models.EmailField(null=False, blank=False)
    text = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.user_email
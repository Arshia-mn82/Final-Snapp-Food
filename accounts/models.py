from django.contrib.auth.models import User
from django.db import models
import secrets

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    x = models.FloatField()
    y = models.FloatField()
    address = models.TextField()
    is_pro = models.BooleanField(default=False)

class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    amount = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.user.username

class APIKey(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=50, unique=True, default=secrets.token_urlsafe)

    def regenerate_key(self):
        self.key = secrets.token_urlsafe(50)
        self.save()

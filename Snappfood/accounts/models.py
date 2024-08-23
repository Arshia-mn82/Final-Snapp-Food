from django.contrib.auth.models import User
from django.db import models



class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    x = models.FloatField()
    y = models.FloatField()
    address = models.TextField()

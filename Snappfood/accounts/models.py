from django.contrib.auth.models import User
from django.db import models



class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    x = models.FloatField()
    y = models.FloatField()
    address = models.TextField()
    
class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    amount = models.PositiveBigIntegerField(default=0)

    def __str__(self) -> str:
        return self.user.username
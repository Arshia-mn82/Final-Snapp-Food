from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User , on_delete=models.CASCADE)
    x = models.FloatField()
    y = models.FloatField()
    phone_number = models.CharField(max_length=11)
    created = models.DateTimeField()
    
    
    def __str__(self) -> str:
        return self.name

from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    x = models.FloatField()
    y = models.FloatField()
    phone_number = models.CharField(max_length=11)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category)
    is_pro = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name

from django.db import models
from django.contrib.auth.models import User
from restaurant_app.models import Restaurant


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Food(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=200)
    price = models.FloatField()
    about = models.TextField()
    stock = models.IntegerField()
    created = models.DateField()
    update = models.DateTimeField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    discount_rate = models.IntegerField()

    def __str__(self) -> str:
        return self.name


class Rate(models.Model):
    rate = models.FloatField()
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> float:
        return self.rate

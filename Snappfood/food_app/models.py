from django.db import models
from django.contrib.auth.models import User
from restaurant_app.models import Restaurant


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Food(models.Model):
    category = models.ManyToManyField(Category)
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=200)
    price = models.FloatField()
    about = models.TextField()
    stock = models.IntegerField()
    created = models.DateField(auto_now=True)
    update = models.DateTimeField(auto_now_add=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    discount_spachial = models.BooleanField(default=False)
    discount_rate = models.IntegerField(null=True,blank=True)

    def total_rating(self):
        return sum([food.get_rate() for food in self.frate.all()])

    def final_price(self):
        if self.discount_rate:
            discount_amount = (self.price * self.discount_rate) / 100
            return self.price - discount_amount
        return self.price


def __str__(self) -> str:
        return self.name


class Rate(models.Model):
    rate = models.FloatField()
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='frate')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_rate(self):
        return self.rate

    def __str__(self) -> float:
        return self.rate

from django.db import models
from django.contrib.auth.models import User
from food_app.models import Food


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    delivery_cost = models.IntegerField(null=True, blank=True)

    def total_price(self):
        return sum([order.total_price() for order in self.oorderitem.all()])

    def __str__(self) -> str:
        return self.user.username


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='oorderitem')
    foods = models.ForeignKey(Food, on_delete=models.CASCADE)
    price = models.FloatField()
    num = models.IntegerField()

    def total_price(self):
        return self.price * self.num


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    order = models.OneToOneField(Order, on_delete=models.CASCADE)

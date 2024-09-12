from django.db import models
from django.contrib.auth.models import User
from food_app.models import Food


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    delivery_cost = models.IntegerField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ("Pending", "Pending"),
            ("Preparing", "Preparing"),
            ("Delivered", "Delivered"),
            ("Cancelled", "Cancelled"),
        ],
        default="Pending",
    )

    @property
    def total_price(self):
        return sum([item.total_price() for item in self.oorderitem.all()])

    def __str__(self) -> str:
        return self.user.username


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="oorderitem"
    )
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    num = models.IntegerField()

    @property
    def total_price(self):
        return self.food.price * self.num


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    order = models.OneToOneField(Order, on_delete=models.CASCADE)

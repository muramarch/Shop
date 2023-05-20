from django.contrib.auth.models import User
from django.db import models

from apps.shops.models import Product

class Cart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )


class CartItem(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE
    )
    quantity = models.IntegerField()


class Order(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    ) 


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE
    )
    order = models.ForeignKey(
        Order, 
        on_delete=models.CASCADE
        )
    quantity = models.IntegerField()

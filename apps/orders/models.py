from django.db import models
from django.contrib.auth import get_user_model
from apps.shops.models import Product

User = get_user_model()

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    created_at = models.DateTimeField(auto_now_add=True)
    # Добавьте другие поля, если необходимо

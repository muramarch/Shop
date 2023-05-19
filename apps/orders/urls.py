from django.urls import path
from .views import view_orders, create_order

urlpatterns = [
    # Добавьте другие URL-маршруты при необходимости
    path('orders/', view_orders, name='view_orders'),
    path('orders/create/', create_order, name='create_order'),
]

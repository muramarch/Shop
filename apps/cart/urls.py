from django.urls import path
from .views import view_cart, add_to_cart, remove_from_cart, checkout

urlpatterns = [
    path('cart/', view_cart, name='view_cart'),
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/checkout/', checkout, name='checkout'),
]

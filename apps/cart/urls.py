from django.urls import path

from .views import order_confirmation, save_order_info, view_cart, add_to_cart, remove_from_cart, place_order

urlpatterns = [
    path('cart/', view_cart, name='view_cart'),
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/place_order/', place_order, name='place_order'),
    path('cart/save_order_info/', save_order_info, name='save_order_info'),
    path('cart/order_confirmation/', order_confirmation, name='order_confirmation'),
]

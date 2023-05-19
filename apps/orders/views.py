from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from apps.cart.models import Cart, CartItem
from .models import Order

@login_required
def view_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'order/view_orders.html', {'orders': orders})

@login_required
def create_order(request):
    # Получите товары из корзины пользователя
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    products = [item.product for item in cart_items]

    # Создайте новый заказ
    order = Order.objects.create(user=request.user)
    order.products.set(products)

    # Очистите корзину
    cart_items.delete()

    return render(request, 'order/order_created.html', {'order': order})

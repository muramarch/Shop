from django.shortcuts import render

from django.shortcuts import render, redirect

from apps.shops.models import Product
from .models import Cart, CartItem

def view_cart(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    return render(request, 'cart/view_cart.html', {'cart_items': cart_items})

def add_to_cart(request, product_id):
    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        cart = Cart.objects.create(user=request.user)
    
    product = Product.objects.get(id=product_id)

    # Проверяем, есть ли уже такой товар в корзине
    try:
        cart_item = CartItem.objects.get(cart=cart, product=product)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(cart=cart, product=product, quantity=1)

    return redirect('view_cart')


def remove_from_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    cart_item.delete()
    return redirect('view_cart')

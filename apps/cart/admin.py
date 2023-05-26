from django.contrib import admin
from .models import Cart, CartItem, Order, OrderItem

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]
    list_display = ('id', 'user')
    search_fields = ('user__username',)

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'cart', 'quantity')
    list_filter = ('cart', 'product')
    search_fields = ('cart__user__username', 'product__name')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity', 'user_full_name', 'user_email')
    list_filter = ('order', 'product')

    def user_full_name(self, obj):
        return obj.order.user.get_full_name()
    user_full_name.short_description = 'User Full Name'
    user_full_name.admin_order_field = 'order__user__first_name'

    def user_email(self, obj):
        return obj.order.user.email
    user_email.short_description = 'User Email' 
    user_email.admin_order_field = 'order__user__email'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    search_fields = ('user__username',)
    list_filter = ('user',)

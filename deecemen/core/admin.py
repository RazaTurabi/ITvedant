from django.contrib import admin
from .models import (
    DeeceCategory,
    DeeceCategory2,
    Product,
    Product2,
    CustomerDetails,
    Payment,
    Order,
    Cart,
    CartItem
)

# --- Existing Models ---

@admin.register(DeeceCategory)
class DeeceCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'small_descp', 'desc', 'og_price', 'image']


@admin.register(DeeceCategory2)
class DeeceCategory2Admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'color', 'size', 'small_descp', 'description', 'price', 'image']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'color', 'size', 'image', 'description']


@admin.register(Product2)
class Product2Admin(admin.ModelAdmin):  # Changed class name to avoid duplicate
    list_display = ['name', 'price', 'color', 'size', 'image', 'description']


@admin.register(CustomerDetails)
class CustomerDetailsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address', 'phone', 'state', 'city', 'pincode']

# --- New Models (Payment, Order, Cart, CartItem) ---

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'order_id', 'payment_id', 'payment_status', 'amount', 'payment_date')
    search_fields = ('payment_id', 'order_id', 'user__username', 'payment_status')
    list_filter = ('payment_status', 'payment_date')
    ordering = ('-payment_date',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'payment', 'created_at', 'status')
    search_fields = ('user__username', 'payment__order_id')
    list_filter = ('status', 'created_at')
    ordering = ('-created_at',)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at')
    search_fields = ('user__username',)
    ordering = ('-created_at',)


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'product', 'product2', 'deece_category', 'quantity')
    list_filter = ('cart',)

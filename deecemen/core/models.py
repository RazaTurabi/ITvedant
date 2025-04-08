from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


# Create your models here.


class DeeceCategory(models.Model):
    CATEGORY_CHOICES = [
        ('MEN', 'Men'),
        ('WOMEN', 'Women'),
        ('KIDS', 'Kids'),
        ('HOODJACK', 'Hoodjack'),
        ('ACCESSORIES', 'Accessories'),
    ]

    name = models.CharField(max_length=250)
    category = models.CharField(max_length=250, choices=CATEGORY_CHOICES)
    small_descp = models.CharField(max_length=250)
    desc = models.TextField()
    og_price = models.IntegerField()
    image = models.ImageField(upload_to='core/')


    def __str__(self):
        return (self.name)
    

class DeeceCategory2(models.Model):
    CATEGORY_CHOICES = [
        ('MEN', 'Men'),
        ('WOMEN', 'Women'),
        ('KIDS', 'Kids'),
        ('HOODJACK', 'Hoodjack'),
        ('FOOTWEAR', 'Footwear'),
    ]

    name = models.CharField(max_length=250)
    category = models.CharField(max_length=250, choices=CATEGORY_CHOICES)
    small_descp = models.CharField(max_length=250)
    description = models.TextField(max_length=500, blank=True)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(upload_to='core_dc_2/')


    def __str__(self):
        return (self.name)
    


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)  # Image field
    description = models.TextField(max_length=500, blank=True)  # Small description field
    
    def __str__(self):
        return self.name


class Product2(models.Model):
    name = models.CharField(max_length=255)
    
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    image = models.ImageField(upload_to='product_images2/', null=True, blank=True)  # Image field
    description = models.TextField(max_length=500, blank=True)  # Small description field
    
    def __str__(self):
        return self.name
    



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cart")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Cart of {self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey('Product', null=True, blank=True, on_delete=models.CASCADE)
    product2 = models.ForeignKey('Product2', null=True, blank=True, on_delete=models.CASCADE)
    deece_category = models.ForeignKey('DeeceCategory2', null=True, blank=True, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        if self.product:
            return f"{self.product.name} - Quantity: {self.quantity}"
        elif self.product2:
            return f"{self.product2.name} - Quantity: {self.quantity}"
        elif self.deece_category:
            return f"{self.deece_category.name} - Quantity: {self.quantity}"

    @property
    def product_instance(self):
        if self.product:
            return self.product
        elif self.product2:
            return self.product2
        elif self.deece_category:
            return self.deece_category
        else:
            return None  # Handle the case where no valid product is set


class CustomerDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=10)
    state = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    pincode = models.IntegerField(default=0, blank=True, null=True)


    def __str__(self):
        return str(self.id)
    
from django.db import models
from django.contrib.auth.models import User

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=255)
    payment_id = models.CharField(max_length=255)
    payment_status = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for {self.user.username} - {self.order_id}"
    
class Subscription(models.Model):
    email = models.EmailField()

from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', on_delete=models.SET_NULL, null=True, blank=True)
    payment = models.ForeignKey('Payment', on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=(
        ("Pending", "Pending"),
        ("Confirmed", "Confirmed"),
        ("Shipped", "Shipped"),
        ("Delivered", "Delivered"),
        ("Cancelled", "Cancelled"),
    ), default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Make sure this is set like this
    address = models.ForeignKey(CustomerDetails, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"


class OrderedItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='ordered_items')
    product_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product_name} x {self.quantity}"

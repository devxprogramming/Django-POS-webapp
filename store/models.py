from django.db import models

from django.utils import timezone
import datetime
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    category = models.ManyToManyField('Category', related_name='category')
    price = models.DecimalField(decimal_places=2, max_digits=90000,null=True)
    quantity = models.IntegerField(null=True)
    manufacturing_date = models.DateTimeField(null=True)
    expiry_date = models.DateTimeField(null=True)
    status = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
        
        
    def __str__(self):
        return f"{self.name}"
        
class Category(models.Model):
    name = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
    
    
    
class Sale(models.Model):
    customer_name = models.CharField(max_length=2000, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(null=True)
    phone = models.CharField(max_length=20, null=True)
    address = models.TextField(null=True)
    issued_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date_issued = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.product

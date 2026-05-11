from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    landing_page_image = models.ImageField(upload_to='landing/')
    description = models.TextField()

class ProductCapacity(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='capacities')
    capacity_name = models.CharField(max_length=10)
    # extra_price = models.IntegerField(default=0)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/image/')
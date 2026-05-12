from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='등록일시')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일시')

    class Meta:
        abstract = True


class Category(TimeStampedModel):
    name = models.CharField(max_length=20, verbose_name='카테고리명')

    def __str__(self):
        return self.name


class Product(TimeStampedModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100, verbose_name='상품이름')
    price = models.PositiveIntegerField(verbose_name='가격')
    landing_page_image = models.ImageField(upload_to='landing/', verbose_name='상품설명이미지')
    description = models.TextField(verbose_name='상세설명')

    def __str__(self):
        return self.name


class ProductCapacity(TimeStampedModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='capacities')
    capacity_name = models.CharField(max_length=10, verbose_name='용량')
    # extra_price = models.IntegerField(default=0, verbose_name='추가금액')

    def __str__(self):
        return f"{self.product.name} — {self.capacity_name}"


class ProductImage(TimeStampedModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/image/', verbose_name='제품이미지')
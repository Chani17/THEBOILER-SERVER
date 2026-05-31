from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='등록일시')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일시')

    class Meta:
        abstract = True


class Classification(TimeStampedModel):
    name = models.CharField(max_length=50, verbose_name='분류 이름')

    def __str__(self):
        return self.name


class Category(TimeStampedModel):
    name = models.CharField(max_length=50, verbose_name='카테고리 이름')
    classification = models.ForeignKey(Classification, on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
        return self.name


class Product(TimeStampedModel):
    name = models.CharField(max_length=50, verbose_name='상품 이름')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name


class Brand(TimeStampedModel):
    name = models.CharField(max_length=50, verbose_name='브랜드 이름')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='brands')

    def __str__(self):
        return self.name


class Model(TimeStampedModel):
    code = models.CharField(max_length=50, verbose_name='모델 이름')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='models')
    
    def __str__(self):
        return self.code


class Image(TimeStampedModel):
    path = models.ImageField(upload_to='products/image/', verbose_name='제품 이미지')
    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.path


class Type(TimeStampedModel):
    name = models.CharField(max_length=100, verbose_name='유형')
    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='types')

    def __str__(self):
        return self.name


class Feature(TimeStampedModel):
    feature = models.CharField(max_length=50, verbose_name='특징')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='features')

    def __str__(self):
        return self.feature


class OptionGroup(TimeStampedModel):
    name = models.CharField(max_length=50, verbose_name='옵션 그룹 이름')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='option_groups')

    def __str__(self):
        return self.name


class OptionValue(TimeStampedModel):
    value = models.CharField(max_length=100, verbose_name='옵션 값')
    option_group = models.ForeignKey(OptionGroup, on_delete=models.CASCADE, related_name='option_values')

    def __str__(self):
        return self.value


class Capacity(TimeStampedModel):
    capacity = models.CharField(max_length=50, verbose_name='용량')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='capacities')

    def __str__(self):
        return self.capacity
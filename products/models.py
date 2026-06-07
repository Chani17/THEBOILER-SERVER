from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='등록일시')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일시')

    class Meta:
        abstract = True


def get_image_upload_path(instance, filename):
    """
    제품 이미지 저장 경로 설정
    경로 형식: products/images/{classification_name}/{category}/{product}/{brand}/{model_code}/{filename}
    """
    try:
        model = instance.model
        brand = model.brand
        product = model.product
        category = product.category
        classification = category.classification

        # 공백을 언더바(_)로 치환하여 경로 안정성 확보
        classification_name = classification.name.replace(" ", "_")
        category_name = category.name.replace(" ", "_")
        product_name = product.name.replace(" ", "_")
        brand_name = brand.name.replace(" ", "_")
        model_code = model.code.replace(" ", "_")

        # 최종 경로 조합
        return f'products/images/{classification_name}/{category_name}/{product_name}/{brand_name}/{model_code}/{filename}'

    except AttributeError:
        # 관계 설정에 문제가 있을 경우를 대비한 대체 경로
        return f'products/images/others/{filename}'


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

    def __str__(self):
        return self.name


class Model(TimeStampedModel):
    code = models.CharField(max_length=50, verbose_name='모델 이름')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='models')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='models')
    
    def __str__(self):
        return self.code


class Image(TimeStampedModel):
    path = models.ImageField(upload_to=get_image_upload_path, verbose_name='제품 이미지')
    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.path.name if self.path else "No Image"


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

from rest_framework import serializers
from .models import Product, Brand, Model

class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = ['id', 'code']


class BrandSerializer(serializers.ModelSerializer):
    models = ModelSerializer(many=True, read_only=True)

    class Meta:
        model = Brand
        fields = ['id', 'name', 'models']


class ProductListSerializer(serializers.ModelSerializer):
    classification = serializers.ReadOnlyField(source='category.classification.name')
    category = serializers.ReadOnlyField(source='category.name')
    # many=True를 붙여서 List<BrandModelSerializer> 형태로 만든다.
    # source='models'는 models.py의 related_name='models'를 찾아가라는 뜻
    brands = BrandSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'classification', 'category', 'brands']



from rest_framework import serializers
from .models import Product, Model, Image, Type, Capacity


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'path']


class CapacitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Capacity
        fields = ['id', 'capacity']

        
class TypeSerializer(serializers.ModelSerializer):
    capacities = CapacitySerializer(many=True, read_only=True)

    class Meta:
        model = Type
        fields = ['id', 'name', 'capacities']


class ModelSerializer(serializers.ModelSerializer):
    brand_name = serializers.ReadOnlyField(source='brand.name')

    class Meta:
        model = Model
        fields = ['id', 'code', 'brand_name']


class ProductListSerializer(serializers.ModelSerializer):
    classification = serializers.ReadOnlyField(source='category.classification.name')
    category = serializers.ReadOnlyField(source='category.name')
    # many=True를 붙여서 List<ModelSerializer> 형태로 만든다.
    # source='models'는 models.py의 Model.product에 설정된 related_name='models'를 찾아가라는 뜻
    models = ModelSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'classification', 'category', 'models']


# 상세 조회를 위한 Serializer
class ModelDetailSerializer(serializers.ModelSerializer):
    brand_name = serializers.ReadOnlyField(source='brand.name')
    product_name = serializers.ReadOnlyField(source='product.name')
    category_name = serializers.ReadOnlyField(source='product.category.name')

    # Nested Serializer: 연관된 이미지와 타입 정보들을 리스트로 포함
    images = ImageSerializer(many=True, read_only=True)
    types = TypeSerializer(many=True, read_only=True)

    class Meta:
        model = Model
        fields = ['id', 'code', 'category_name', 'product_name', 'brand_name', 'images', 'types']

from rest_framework import serializers
from .models import Product, Model

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




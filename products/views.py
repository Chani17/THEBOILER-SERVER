from rest_framework import generics
from .models import Product, Model
from .serializers import ProductListSerializer, ModelDetailSerializer
from django.db.models import Prefetch

class ProductListView(generics.ListAPIView):
    serializer_class = ProductListSerializer

    def get_queryset(self):
        # Query Parameter 추출
        classification_name = self.request.query_params.get('classification')
        category_name = self.request.query_params.get('category')

        # 쿼리 최적화
        queryset = Product.objects.select_related(
            'category',
            'category__classification'
        ).prefetch_related(
            'models__brand',
        )

        # 동적 쿼리문
        if classification_name:
            queryset = queryset.filter(category__classification__name=classification_name)

        if category_name:
            queryset = queryset.filter(category__name=category_name)

        return queryset


class ModelDetailView(generics.RetrieveAPIView):
    serializer_class = ModelDetailSerializer

    def get_queryset(self):
        # 모든 관계 데이터를 한 번에 Join/Fetch 해오도록 쿼리 최적화
        return Model.objects.all().select_related(
            'brand',
            'product__category'
        ).prefetch_related(
            'images',
            'types__capacities'
        )
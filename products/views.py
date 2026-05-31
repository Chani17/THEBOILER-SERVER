from rest_framework import generics
from .models import Product, Model
from .serializers import ProductListSerializer
from django.db.models import Prefetch

class ProductListView(generics.ListAPIView):
    serializer_class = ProductListSerializer

    def get_queryset(self):
        # Query Parameter 추출
        classification_id = self.request.query_params.get('classification')
        category_id = self.request.query_params.get('category')

        # 쿼리 최적화
        queryset = Product.objects.select_related(
            'category',
            'category__classification'
        ).prefetch_related(
            'brands__models'
        )

        # 동적 쿼리문
        if classification_id:
            queryset = queryset.filter(category__classification__name=classification_id)

        if category_id:
            queryset = queryset.filter(category__name=category_id)

        return queryset
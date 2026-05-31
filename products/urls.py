from django.urls import path
from .views import ProductListView

urlpatterns = [
    # GET /products
    path('', ProductListView.as_view(), name='product-list'),
]

from django.urls import path
from .views import ProductListView, ModelDetailView

urlpatterns = [
    # GET /products
    path('', ProductListView.as_view(), name='product-list'),
    path('models/<int:id>/', ModelDetailView.as_view(), name='model-detail')
]

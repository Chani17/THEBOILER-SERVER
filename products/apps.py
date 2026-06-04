from django.apps import AppConfig


class ProductsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "products"
    verbose_name = "Products (제품 관리)"

    def get_models(self, *args, **kwargs):
        # Admin 사이드바에서 보여질 모델의 순서를 지정합니다.
        ordered_models = [
            'Classification',
            'Category',
            'Product',
            'Brand',
            'Model',
            'Type',
            'Capacity',
            'Image',
            'Feature',
            'OptionGroup',
            'OptionValue',
        ]
        
        models = super().get_models(*args, **kwargs)
        # ordered_models에 정의된 순서대로 정렬, 리스트에 없으면 뒤로 보냄(999)
        return sorted(models, key=lambda m: ordered_models.index(m.__name__) if m.__name__ in ordered_models else 999)

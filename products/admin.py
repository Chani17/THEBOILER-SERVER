from django.contrib import admin
from .models import Category, Product, ProductCapacity, ProductImage


class ProductCapacityInline(admin.TabularInline):
    model = ProductCapacity
    extra = 1


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "created_at", "updated_at")
    list_filter = ("category",)
    search_fields = ("name", "description")
    inlines = (ProductCapacityInline, ProductImageInline)


@admin.register(ProductCapacity)
class ProductCapacityAdmin(admin.ModelAdmin):
    list_display = ("capacity_name", "product", "created_at", "updated_at")
    list_filter = ("product",)
    search_fields = ("capacity_name", "product__name")


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("product", "image", "created_at", "updated_at")
    list_filter = ("product",)
    search_fields = ("product__name",)

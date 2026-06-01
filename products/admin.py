from django.contrib import admin
from .models import (
    Brand,
    Capacity,
    Category,
    Classification,
    Feature,
    Image,
    Model,
    OptionGroup,
    OptionValue,
    Product,
    Type,
)


# --- Inlines ---
class CategoryInline(admin.TabularInline):
    model = Category
    extra = 1


class ProductInline(admin.TabularInline):
    model = Product
    extra = 1


class ModelInlineForProduct(admin.TabularInline):
    model = Model
    fields = ("code", "brand")
    extra = 1


class ModelInlineForBrand(admin.TabularInline):
    model = Model
    fields = ("code", "product")
    extra = 1


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1


class TypeInline(admin.TabularInline):
    model = Type
    extra = 1


class FeatureInline(admin.TabularInline):
    model = Feature
    extra = 1


class OptionGroupInline(admin.TabularInline):
    model = OptionGroup
    extra = 1


class OptionValueInline(admin.TabularInline):
    model = OptionValue
    extra = 1


class CapacityInline(admin.TabularInline):
    model = Capacity
    extra = 1


# --- ModelAdmin ---

@admin.register(Classification)
class ClassificationAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    search_fields = ("name",)
    inlines = (CategoryInline,)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "classification", "created_at", "updated_at")
    list_filter = ("classification",)
    search_fields = ("name",)
    inlines = (ProductInline,)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "created_at", "updated_at")
    list_filter = ("category",)
    search_fields = ("name",)
    inlines = (ModelInlineForProduct,)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    search_fields = ("name",)
    inlines = (ModelInlineForBrand,)


@admin.register(Model)
class BoilerModelAdmin(admin.ModelAdmin):
    list_display = (
        "code",
        "product",
        "brand",
        "get_category",
        "get_classification",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "brand",
        "product",
        "product__category",
        "product__category__classification",
    )
    search_fields = (
        "code",
        "brand__name",
        "product__name",
        "product__category__name",
        "product__category__classification__name",
    )
    readonly_fields = ("get_category", "get_classification")
    fields = ("get_classification", "get_category", "product", "brand", "code")
    inlines = (ImageInline, TypeInline)

    @admin.display(description="카테고리")
    def get_category(self, obj):
        if obj.product_id:
            return obj.product.category
        return "-"

    @admin.display(description="분류")
    def get_classification(self, obj):
        if obj.product_id and obj.product.category_id:
            return obj.product.category.classification
        return "-"


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("path", "model", "created_at", "updated_at")
    list_filter = ("model",)
    search_fields = ("model__code",)


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ("name", "model", "created_at", "updated_at")
    list_filter = ("model",)
    search_fields = ("name", "model__code")
    inlines = (FeatureInline, OptionGroupInline, CapacityInline)


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ("feature", "type", "created_at", "updated_at")
    list_filter = ("type",)
    search_fields = ("feature", "type__name")


@admin.register(OptionGroup)
class OptionGroupAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "created_at", "updated_at")
    list_filter = ("type",)
    search_fields = ("name",)
    inlines = (OptionValueInline,)


@admin.register(OptionValue)
class OptionValueAdmin(admin.ModelAdmin):
    list_display = ("value", "option_group", "created_at", "updated_at")
    list_filter = ("option_group",)
    search_fields = ("value", "option_group__name")


@admin.register(Capacity)
class CapacityAdmin(admin.ModelAdmin):
    list_display = ("capacity", "type", "created_at", "updated_at")
    list_filter = ("type",)
    search_fields = ("capacity", "type__name")

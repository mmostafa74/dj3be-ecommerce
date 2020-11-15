from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "slug"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "price", "availabe", "created", "updated"]
    list_filter = ["availabe", "created", "updated"]
    list_editable = ["price", "availabe"]
    prepopulated_fields = {"slug": ("name",)}

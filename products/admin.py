from products.models import Category
from django.contrib import admin
from . import models
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','price', 'category', 'sub_category', 'image')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent')

admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.SubCategory, SubCategoryAdmin)

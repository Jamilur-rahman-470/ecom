from django.contrib import admin
from .models import Product, Category, SubCategory
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category',
                    'sub_category', 'price', 'slug', 'discounted_price']
    exclude = ['discounted_price']

    prepopulated_fields = {
        'slug': ('name',),
    }


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    class Meta:
        exclude = ('slug',)


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'parent', 'slug']
    prepopulated_fields = {
        'slug': ('name',),
    }
        

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
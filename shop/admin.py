from django.contrib import admin
from .models import Order, OrderItem, Product, Category, SubCategory
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
        
class OrderItemAdmin(admin.ModelAdmin):
    list_display = [ 'owner', 'product', 'is_ordered']
    
    
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','ref_code', 'is_shipped', 'owner']
    
        

admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)

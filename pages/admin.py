from django.contrib import admin
from .models import Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


admin.site.register(Contact, ContactAdmin)
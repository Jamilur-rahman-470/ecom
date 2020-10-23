from django.contrib import admin
from .models import AddressAndInfo, Profile
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']

class AddressAndInfoAdmin(admin.ModelAdmin):
    list_display = ['country', 'user']

admin.site.register(AddressAndInfo, AddressAndInfoAdmin)
admin.site.register(Profile, ProfileAdmin)

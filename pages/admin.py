from django.contrib import admin

# Register your models here.
from pages.models import ContactModel, BannerModel

@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']
    list_filter = ['created_at']


@admin.register(BannerModel)
class BannerModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'collection', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'collection', 'description']


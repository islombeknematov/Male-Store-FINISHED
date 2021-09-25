from django.contrib import admin

# Register your models here.
from users.models import ProfileModel, CouponModel


@admin.register(ProfileModel)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name']


@admin.register(CouponModel)
class CouponModelAdmin(admin.ModelAdmin):
    list_display = ['code', 'amount', 'created_at', 'is_used']
    search_fields = ['code']

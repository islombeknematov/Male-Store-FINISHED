from django.contrib import admin

# Register your models here.
from orders.models import OrderModel


@admin.register(OrderModel)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at']

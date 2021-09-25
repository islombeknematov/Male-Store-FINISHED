from django.contrib import admin
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin

from products.forms import ColorAdminForm
from products.models import CategoryModel, ProductTagModel, ProductModel, BrandModel, ColorModel, SizeModel


# Register your models here.

@admin.register(CategoryModel)
class CategoryModelAdmin(TranslationAdmin):

    # list_display_links = ['created_at']

    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(ProductModel)
class ProductModelAdmin(TranslationAdmin):

    # list_display_links = ['created_at']

    list_display = ['title', 'price', 'discount', 'created_at']
    list_filter = ['category', 'tags', 'created_at']
    search_fields = ['title']
    autocomplete_fields = ['category', 'tags', 'brand', 'colors', 'sizes']

    readonly_fields = ['real_price']

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(ProductTagModel)
class ProductTagModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(BrandModel)
class BrandModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(ColorModel)
class ColorModelAdmin(admin.ModelAdmin):
    list_display = ['code', 'color', 'created_at']
    list_filter = ['created_at']
    search_fields = ['code']
    form = ColorAdminForm

    def color(self, obj):
        return mark_safe(f'<div style="background-color: {obj.code}">&nbsp</div>')


@admin.register(SizeModel)
class SizeModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']




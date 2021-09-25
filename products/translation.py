

from modeltranslation.translator import register, TranslationOptions

from products.models import ProductModel, CategoryModel


@register(ProductModel)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'long_description',)


@register(CategoryModel)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)






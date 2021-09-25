from django.contrib.auth import get_user_model

from django.db import models, IntegrityError
from django.utils import timezone
from django.utils.translation import gettext as _


UserModel = get_user_model()

# Create your models here.


class CategoryModel(models.Model):
    title = models.CharField(max_length=32, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")


class ProductTagModel(models.Model):
    title = models.CharField(max_length=32, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("product tag")
        verbose_name_plural = _("product tags")


class BrandModel(models.Model):
    title = models.CharField(max_length=32, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True, )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('brand')
        verbose_name_plural = _('brands')


class ColorModel(models.Model):
    code = models.CharField(max_length=32, verbose_name=_('code'))
    created_at = models.DateTimeField(auto_now_add=True, )

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = _('color')
        verbose_name_plural = _('colors')


class SizeModel(models.Model):
    title = models.CharField(max_length=32, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True, )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('size')
        verbose_name_plural = _('sizes')


class ProductModel(models.Model):
    title = models.CharField(max_length=128, verbose_name=_('title'))
    image = models.ImageField(upload_to='products', verbose_name=_('image'))
    price = models.FloatField(verbose_name=_('price'))
    real_price = models.FloatField(default=0, verbose_name=_('real price'))
    discount = models.PositiveSmallIntegerField(default=0)
    short_description = models.TextField(verbose_name=_("short description"))
    long_description = models.TextField(verbose_name=_("long description"))

    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.PROTECT,
        related_name='products',
        verbose_name=_("category")
    )

    brand = models.ForeignKey(
        BrandModel,
        on_delete=models.PROTECT,
        related_name='products',
        verbose_name=_("brand"),
        null=True
    )

    colors = models.ManyToManyField(
        ColorModel,
        related_name='products',
        verbose_name=_("color")
    )

    sizes = models.ManyToManyField(
        SizeModel,
        related_name='products',
        verbose_name=_("size"),
    )

    tags = models.ManyToManyField(
        ProductTagModel,
        related_name='products',
        verbose_name=_('tags')

    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def is_discount(self):
        return self.discount != 0

    def is_new(self):
        return (timezone.now() - self.created_at).days <= 3

    def get_related(self):
        return self.category.products.order_by('-pk').exclude(pk=self.pk)[:4]


    @staticmethod
    def get_from_cart(cart):
        return ProductModel.objects.filter(pk__in=cart)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")



class WishlistModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='wishlist')
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='wishlist')


    def __str__(self):
        return f'{self.user.get_full_name()} | {self.product.title}'


    @staticmethod
    def add_or_delete(user, product):
        try:
            WishlistModel.objects.create(user=user, product=product)
        except IntegrityError:
            WishlistModel.objects.get(user=user, product=product).delete()



    class Meta:
        verbose_name = _('wishlist')
        verbose_name_plural = _('wishlist')
        unique_together = 'user', 'product',






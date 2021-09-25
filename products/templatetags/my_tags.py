from django.db.models import Sum
from django.template import Library

from products.models import WishlistModel, ProductModel
from users.models import ProfileModel

register = Library()

@register.simple_tag
def get_default_range(request):
    price = request.GET.get('price_filter')
    if price:
        price_from, price_to = price.split(';')
        return f'from: {price_from}, to: {price_to},'
    return ''


@register.simple_tag
def get_cart_info(request):
    cart = request.session.get('cart', [])

    if not cart:
        return 0, 0.0

    return len(cart), ProductModel.get_from_cart(cart).aggregate(
        Sum('real_price')
    )['real_price__sum']


@register.filter
def in_wishlist(product, user):
    return WishlistModel.objects.filter(user=user, product=product).exists()


@register.filter
def in_cart(product, request):
    return product.pk in request.session.get('cart', [])


@register.filter
def replace(text, pattern):
    text = str(text)
    return text.replace(pattern[0], pattern[1])


@register.simple_tag
def get_total(amount, request):
    profile = ProfileModel.objects.get(user=request.user)

    return profile.get_total(amount)[0]


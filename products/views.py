from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Max, Min
from django.shortcuts import get_object_or_404, redirect

# Create your views here.
from django.views.generic import ListView, DetailView
from products.models import ProductModel, CategoryModel, ProductTagModel, BrandModel, ColorModel, SizeModel, \
    WishlistModel


class ProductsListView(ListView):
    template_name = 'shop.html'
    paginate_by = 3


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['categories'] = CategoryModel.objects.all()
        context['tags'] = ProductTagModel.objects.all()
        context['brands'] = BrandModel.objects.all()
        context['sizes'] = SizeModel.objects.all()
        context['colors'] = ColorModel.objects.all()
        context['max_price'], context['min_price'] = ProductModel.objects.aggregate(
            Max('real_price'), Min('real_price')
        ).values()

        return context


    def get_queryset(self):
        qs = ProductModel.objects.all()

        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(title__icontains=q)


        categ = self.request.GET.get('categ')
        if categ:
            qs = qs.filter(category_id=categ)


        tag = self.request.GET.get('tag')
        if tag:
            qs = qs.filter(tags__id=tag)

        color = self1.request.GET.get('color')
        if color:
            qs = qs.filter(colors__id=color)

        size = self.request.GET.get('size')
        if size:
            qs = qs.filter(sizes__id=size)

        price_filter = self.request.GET.get('price_filter')
        if price_filter:
            price_from, price_to = price_filter.split(';')
            qs = qs.filter(real_price__gte=price_from, real_price__lte=price_to)


        brand = self.request.GET.get('brand')
        if brand:
            qs = qs.filter(brand__id=brand)


        sort = self.request.GET.get('sort')
        if sort == '-price':
            qs = qs.order_by('-price')
        elif sort == 'price':
            qs = qs.order_by('price')

        return qs

class ProductDetailView(DetailView):
    template_name = 'shop-details.html'
    model = ProductModel



class WishlistListView(LoginRequiredMixin, ListView):
    template_name = 'wishlist.html'

    def get_queryset(self):
        return ProductModel.objects.filter(wishlist__user=self.request.user)



@login_required
def update_wishlist(request, pk):
    product = get_object_or_404(ProductModel, pk=pk)
    WishlistModel.add_or_delete(request.user, product)

    return redirect(request.GET.get('next', '/'))


class CartListView(ListView):
    template_name = 'shopping-cart.html'

    def get_queryset(self):
        cart = self.request.session.get('cart', [])
        return ProductModel.get_from_cart(cart)


def update_cart(request, pk):
    product = get_object_or_404(ProductModel, pk=pk)
    cart = request.session.get('cart', [])
    if product.pk in cart:
        cart.remove(product.pk)
    else:
        cart.append(product.pk)
    request.session['cart'] = cart

    print(request.session['cart'])
    return redirect(request.GET.get('next', '/'))








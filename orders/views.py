from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, TemplateView, ListView

from orders.forms import OrderModelForm
from orders.models import OrderModel
from products.models import ProductModel


class CheckoutTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'checkout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        cart = self.request.session.get('cart', [])

        products = ProductModel.get_from_cart(cart)

        context['profile'] = self.request.user.profile
        context['products'] = products
        context['sum'] = products.aggregate(Sum('real_price'))['real_price__sum']

        return context


class OrderCreateView(LoginRequiredMixin, CreateView):
    form_class = OrderModelForm

    def get_success_url(self):
        return reverse('pages:home')


    def form_valid(self, form):
        cart = self.request.session.get('cart', [])
        products = ProductModel.get_from_cart(cart)

        form.instance.user = self.request.user
        total = products.aggregate(Sum('real_price'))['real_price__sum']

        profile = self.request.user.profile
        temp_total, temp_balance = profile.get_total(total)

        form.instance.total_price = temp_total

        order = form.save()

        order.products.set(products)  # set used only with ManyToManyField
        order.save()

        profile.balance = temp_balance
        profile.save()


        self.request.session['cart'] = []

        return redirect(self.get_success_url())




class OrderHistoryListView(LoginRequiredMixin, ListView):
    template_name = 'history.html'

    def get_queryset(self):
        return OrderModel.objects.filter(user=self.request.user)












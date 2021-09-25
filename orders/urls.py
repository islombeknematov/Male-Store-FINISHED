from django.urls import path

from orders.views import OrderCreateView, CheckoutTemplateView, OrderHistoryListView

app_name = 'orders'

urlpatterns = [
    path('history/', OrderHistoryListView.as_view(), name='history'),
    path('checkout/', CheckoutTemplateView.as_view(), name='checkout-view'),
    path('checkout/save/', OrderCreateView.as_view(), name='checkout-save'),
]




from django.urls import path

from users.views import ProfileUpdateView, CouponCheckView

app_name = 'users'

urlpatterns = [
    path('profile/', ProfileUpdateView.as_view(), name='profile'),
    path('coupon/', CouponCheckView.as_view(), name='coupon-check'),
]

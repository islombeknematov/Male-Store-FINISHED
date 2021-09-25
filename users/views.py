from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.shortcuts import  redirect
from django.urls import reverse
from django.views import View
from django.views.generic import UpdateView


from users.forms import ProfileModelForm
from users.models import CouponModel


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'profile.html'
    form_class = ProfileModelForm

    def get_success_url(self):
        return reverse("users:profile")

    def get_object(self, queryset=None):
            return self.request.user.profile



class CouponCheckView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        code = request.POST.get('coupon')
        try:
            coupon = CouponModel.objects.get(code=code, is_used=False)
        except CouponModel.DoesNotExist:
            messages.error(request, 'Coupon does not exist or already used')
            return redirect('products:cart')

        if coupon.in_percent:
            pass
        else:
            profile = request.user.profile
            profile.balance += coupon.amount
            profile.save()

            coupon.is_used = True
            coupon.save()

            messages.success(request, 'Coupon successfully applied')
            return redirect('products:cart')




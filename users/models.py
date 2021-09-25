from django.contrib.auth import get_user_model
from django.db import models

from django.utils.translation import gettext as _

UserModel = get_user_model()


# Create your models here.
class ProfileAbstractModel(models.Model):
    phone = models.CharField(max_length=13, null=True, blank=True)
    email = models.CharField(max_length=32, null=True, blank=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    address1 = models.CharField(max_length=200, null=True, blank=True)
    address2 = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    postcode = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        abstract = True


class ProfileModel(ProfileAbstractModel):
    user = models.OneToOneField(UserModel, related_name='profile', on_delete=models.CASCADE)
    balance = models.PositiveIntegerField(default=0)

    def get_full_name(self):
        fname = self.first_name or ''
        lname = self.last_name or ''
        return f'{fname} {lname}'

    def get_total(self, amount):
        if self.balance > amount:
            return 0, self.balance - amount
        else:
            return amount - self.balance, 0

    def __str__(self):
        return f'Profile: {str(self.user)}'

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profile'


class CouponModel(models.Model):
    code = models.CharField(max_length=8, unique=True, verbose_name=_('code'))
    amount = models.PositiveIntegerField(verbose_name=_('amount'))
    in_percent = models.BooleanField(default=False, verbose_name=_('in percent'))
    is_used = models.BooleanField(default=False, verbose_name=_('is used'))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'coupon'
        verbose_name_plural = 'coupons'

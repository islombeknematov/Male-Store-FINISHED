from django.db import models

# Create your models here.
from products.models import ProductModel
from users.models import ProfileAbstractModel, UserModel


class OrderModel(ProfileAbstractModel):
    user = models.ForeignKey(UserModel, related_name='orders', on_delete=models.CASCADE)
    products = models.ManyToManyField(ProductModel)
    total_price = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):

        return f'Order: {str(self.user)}'

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'



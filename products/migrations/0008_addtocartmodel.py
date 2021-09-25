# Generated by Django 3.2.5 on 2021-08-09 05:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0007_alter_wishlistmodel_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddToCartModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='add_to_cart', to='products.productmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='add_to_cart', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'add_to_cart',
                'verbose_name_plural': 'add_to_cart',
                'unique_together': {('user', 'product')},
            },
        ),
    ]

# Generated by Django 3.2.5 on 2021-07-28 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210721_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='real_price',
            field=models.FloatField(default=0, verbose_name='real price'),
        ),
    ]

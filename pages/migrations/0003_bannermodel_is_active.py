# Generated by Django 3.2.5 on 2021-07-15 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_bannermodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='bannermodel',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='is avtive'),
        ),
    ]
# Generated by Django 3.2.5 on 2021-07-11 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_posttagmodel_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postmodel',
            old_name='context',
            new_name='content',
        ),
    ]

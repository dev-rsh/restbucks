# Generated by Django 3.2.9 on 2021-11-07 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_auto_20211107_2158'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='order_id',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='productattribute',
            old_name='attribute_id',
            new_name='attribute',
        ),
        migrations.RenameField(
            model_name='productattribute',
            old_name='product_id',
            new_name='product',
        ),
    ]

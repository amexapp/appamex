# Generated by Django 4.0.4 on 2022-05-20 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_products_cost_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='cost_sales',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10),
        ),
    ]

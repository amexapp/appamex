from django.db import models
from django.utils import timezone


class ProductsCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=60)
    amount = models.DecimalField(max_digits=9, decimal_places=0, default=0)
    image = models.ManyToManyField('ProductsImage', blank=True)
    cost_product = models.DecimalField(
        max_digits=9, decimal_places=3, default=0)
    cost_sales = models.DecimalField(
        max_digits=10, decimal_places=3, default=0)
    category = models.ForeignKey(ProductsCategory, on_delete=models.PROTECT)
    sku = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class ProductsImage(models.Model):
    image = models.ImageField(
        upload_to='product/%Y/%m/%d', blank=True, null=True)

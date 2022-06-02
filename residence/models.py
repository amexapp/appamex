from pyexpat import model
from django.db import models
from django.utils import timezone


class Product(models.Model):
    productName = models.CharField(max_length=200)
    productDescription = models.TextField(blank=True)
    productPrice = models.DecimalField(
        max_digits=9, decimal_places=0, default=0)

    class Meta:
        db_table = 'products'
        ordering = ['-productName']

    def __str__(self):
        return self.productName


class ProductSet(models.Model):
    quantity = models.PositiveIntegerField()
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    def __str__(self):
        return self.product.productName


class Box(models.Model):
    boxName = models.CharField(max_length=255, blank=False)
    product_set = models.ManyToManyField(ProductSet)

    def __str__(self):
        return self.boxName

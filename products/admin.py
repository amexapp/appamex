from django.contrib import admin
from .models import Products, ProductsCategory, ProductsImage

admin.site.register(Products)
admin.site.register(ProductsCategory)
admin.site.register(ProductsImage)

from django.db import models
from django.utils import timezone
from people.models import People


class PlaceImage(models.Model):
    image = models.ImageField(
        upload_to='place/%Y/%m/%d', blank=True, null=True)


class Place(models.Model):
    name_residence = models.CharField(max_length=30)
    phone = models.CharField(max_length=9)
    addres = models.CharField(max_length=15)
    image = models.ForeignKey(
        PlaceImage, on_delete=models.SET_NULL, related_name='place', null=True)
    Representante = models.ForeignKey(
        People, on_delete=models.SET_NULL, related_name='peoples', null=True)

    def __str__(self):
        return self.name_residence

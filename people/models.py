from django.db import models
from django.utils import timezone


class PeopleSex(models.Model):
    tipo_sex = models.CharField(max_length=10)

    def __str__(self):
        return self.tipo_sex


class People(models.Model):
    rut = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=9)
    addres = models.CharField(max_length=15)
    sex = models.ForeignKey(
        PeopleSex, on_delete=models.CASCADE, related_name='sexo')
    age = models.IntegerField()
    date_birth = models.DateField(blank=True)
    email = models.CharField(max_length=35)
    signature = models.ManyToManyField('SignaImage', blank=True)
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class SignaImage(models.Model):
    image = models.ImageField(upload_to='blog/%Y/%m/%d', blank=True, null=True)

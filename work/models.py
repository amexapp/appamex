from django.db import models
from ckeditor.fields import RichTextField
from place.models import Place
from people.models import People


class States(models.Model):
    tipo_state = models.CharField(max_length=20)

    def __str__(self):
        return self.tipo_state


class StatesPago(models.Model):
    statepago = models.CharField(max_length=20)

    def __str__(self):
        return self.statepago


class Encargado(models.Model):
    rut = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=9)

    def __str__(self):
        return self.name


class Work(models.Model):
    titulo = models.CharField(max_length=50)
    Doc_propuesta = models.ManyToManyField('UploadDoc', blank=True)
    Description = RichTextField(blank=True, null=True)
    date_first = models.DateField()
    date_finish = models.DateField()
    state = models.ForeignKey(
        States, on_delete=models.CASCADE, related_name='estado')
    state_pago = models.ForeignKey(
        StatesPago, on_delete=models.CASCADE, related_name='pago')
    cost_total = models.DecimalField(
        max_digits=9, decimal_places=3, default=0)
    Residencia = models.ForeignKey(Place, on_delete=models.SET_NULL, null=True)
    Encargado = models.ForeignKey(
        Encargado, on_delete=models.SET_NULL, null=True)
    Representan = models.ForeignKey(
        People, on_delete=models.SET_NULL, related_name='Representan', null=True)

    def __str__(self):
        return self.titulo


class UploadDoc(models.Model):
    Document = models.FileField(
        upload_to='uploads/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return self.Document.name

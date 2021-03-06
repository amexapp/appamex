# Generated by Django 4.0.4 on 2022-05-30 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0002_alter_place_representante'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='place/%Y/%m/%d')),
            ],
        ),
        migrations.AddField(
            model_name='place',
            name='image',
            field=models.ManyToManyField(blank=True, to='place.placeimage'),
        ),
    ]

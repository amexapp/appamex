# Generated by Django 4.0.4 on 2022-05-23 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0005_work_representan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='titulo',
            field=models.CharField(max_length=50),
        ),
    ]

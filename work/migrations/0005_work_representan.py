# Generated by Django 4.0.4 on 2022-05-22 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
        ('work', '0004_rename_people_work'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='Representan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Representan', to='people.people'),
        ),
    ]

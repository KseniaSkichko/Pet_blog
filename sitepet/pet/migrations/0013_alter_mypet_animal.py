# Generated by Django 5.0.4 on 2024-04-25 17:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0012_remove_animal_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mypet',
            name='animal',
            field=models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.PROTECT, related_name='animal', to='pet.animal', verbose_name='Вид питомца'),
        ),
    ]

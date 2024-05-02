# Generated by Django 5.0.4 on 2024-05-02 13:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0014_animal_slug_mypet_slug'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='author',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mypet',
            name='animal',
            field=models.OneToOneField(max_length=50, on_delete=django.db.models.deletion.PROTECT, related_name='animal', to='pet.animal', verbose_name='Вид питомца'),
        ),
        migrations.AlterField(
            model_name='mypet',
            name='slug',
            field=models.SlugField(max_length=30, unique=True),
        ),
    ]

# Generated by Django 5.0.4 on 2024-04-25 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0011_remove_mypet_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='slug',
        ),
    ]

# Generated by Django 5.0.4 on 2024-04-19 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0008_uploadfields_alter_tagposts_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='photos/%d/%m/%Y', verbose_name='Файл'),
        ),
    ]

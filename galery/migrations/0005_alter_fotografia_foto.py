# Generated by Django 4.1.5 on 2023-01-13 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("galery", "0004_fotografia_data_fotografia"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fotografia",
            name="foto",
            field=models.ImageField(blank=True, upload_to="fotos/%Y/%m/%d/"),
        ),
    ]
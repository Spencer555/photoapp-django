# Generated by Django 3.2.10 on 2022-02-17 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0005_photo_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
# Generated by Django 3.1.1 on 2021-07-20 17:25

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0006_auto_20210720_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]

# Generated by Django 3.2 on 2021-07-08 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='like',
            field=models.PositiveBigIntegerField(blank=True, default=0, verbose_name='like'),
        ),
    ]

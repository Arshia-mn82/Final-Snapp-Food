# Generated by Django 5.1 on 2024-09-13 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='is_pro',
            field=models.BooleanField(default=False),
        ),
    ]

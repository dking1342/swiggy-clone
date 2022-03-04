# Generated by Django 4.0.3 on 2022-03-04 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_restaurant_restaurant_cost_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='restaurant_rating',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=2),
        ),
    ]

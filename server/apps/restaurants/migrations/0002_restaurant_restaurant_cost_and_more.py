# Generated by Django 4.0.3 on 2022-03-04 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discount', '0001_initial'),
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='restaurant_cost',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='discounts',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='discounts', to='discount.discount'),
        ),
    ]

# Generated by Django 4.0.3 on 2022-03-04 04:26

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('discount', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('restaurant_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('restaurant_name', models.CharField(default='Food Stuff', max_length=50)),
                ('restaurant_address_1', models.CharField(default='123 Main St', max_length=128)),
                ('restaurant_address_2', models.CharField(blank=True, max_length=128)),
                ('restaurant_city', models.CharField(default='New York City', max_length=64)),
                ('restaurant_zip_code', models.CharField(default='90210', max_length=5)),
                ('restaurant_state', models.CharField(choices=[('AL', 'Alabama'), ('CA', 'California'), ('MI', 'Michigan'), ('WI', 'Wisconsin')], default='AL', max_length=2)),
                ('restaurant_cuisines', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=20), size=20)),
                ('restaurant_main_img', models.URLField(default='')),
                ('discount_isValid', models.BooleanField(default=False)),
                ('restaurant_created', models.DateTimeField(auto_now_add=True)),
                ('discounts', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='discount.discount')),
            ],
            options={
                'ordering': ['restaurant_name'],
            },
        ),
    ]

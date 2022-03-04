# Generated by Django 4.0.3 on 2022-03-04 04:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('discount_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('discount_code', models.CharField(max_length=10)),
                ('discount_text', models.CharField(max_length=150)),
                ('discount_amount', models.IntegerField(default=0)),
                ('discount_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

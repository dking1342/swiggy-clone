# Generated by Django 4.0.3 on 2022-03-04 09:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cuisines',
            fields=[
                ('cuisine_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('cuisine_name', models.CharField(default='', max_length=50)),
            ],
            options={
                'ordering': ['cuisine_name'],
            },
        ),
    ]

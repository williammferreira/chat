# Generated by Django 3.2 on 2021-11-14 01:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0008_auto_20211008_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
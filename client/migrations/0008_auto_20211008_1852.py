# Generated by Django 3.2 on 2021-10-08 22:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0007_alter_profile_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='theme',
            field=models.CharField(default='light', max_length=5),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.TextField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterModelTable(
            name='profile',
            table='profile',
        ),
    ]

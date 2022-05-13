# Generated by Django 4.0.3 on 2022-05-07 14:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('client', '0023_rename_temp_id_chats_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chats',
            name='chatCreator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chatCreator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='chats',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

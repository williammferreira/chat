# Generated by Django 4.0.3 on 2022-05-13 14:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0033_alter_chats_chatcreator_alter_chats_chatusers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chats',
            name='locationUrl',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),

        migrations.AddField(
            model_name='chats',
            name='locationUrl',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
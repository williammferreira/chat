# Generated by Django 4.0.3 on 2022-05-13 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0034_alter_chats_locationurl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='chat',
        ),
        migrations.DeleteModel(
            name='chats',
        ),
        migrations.DeleteModel(
            name='messages',
        ),
    ]

# Generated by Django 4.0.3 on 2022-05-06 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0017_remove_chats_id_chats_locationurl_chats_token'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]

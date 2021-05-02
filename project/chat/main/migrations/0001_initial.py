# Generated by Django 3.1.7 on 2021-04-01 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='chats',
            fields=[
                ('chat_creator', models.TextField()),
                ('chat_users', models.TextField()),
                ('chat_name', models.TextField()),
                ('chat_date_created', models.TextField()),
                ('chat_area', models.TextField()),
                ('location_url', models.TextField(default='notworking', primary_key=True, serialize=False)),
            ],
        ),
    ]

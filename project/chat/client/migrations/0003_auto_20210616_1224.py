# Generated by Django 3.2 on 2021-06-16 12:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_alter_messages_randompk'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='randompk',
        ),
        migrations.AddField(
            model_name='messages',
            name='messageId',
            field=models.TextField(default=datetime.datetime(2021, 6, 16, 12, 24, 30, 305428, tzinfo=utc), primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
# Generated by Django 3.2 on 2021-11-23 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0010_alter_messages_chat'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='token',
            field=models.TextField(default='none'),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.2 on 2021-05-21 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chats',
            name='token',
            field=models.TextField(default='test', primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chats',
            name='location_url',
            field=models.TextField(),
        ),
    ]

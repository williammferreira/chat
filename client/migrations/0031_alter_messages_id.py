# Generated by Django 4.0.3 on 2022-05-07 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0030_alter_messages_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
# Generated by Django 4.0.3 on 2022-04-18 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0014_alter_profile_theme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='theme',
            field=models.CharField(choices=[('dark', 'Dark'), ('black', 'Black'), ('bluelines', 'Blue_Lines'), ('light', 'Light')], default='black', max_length=10),
        ),
    ]

# Generated by Django 4.0.3 on 2022-04-27 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0009_appgroup_importance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appgroup',
            name='importance',
            field=models.PositiveIntegerField(default=4, verbose_name='importance'),
        ),
    ]

# Generated by Django 4.0.3 on 2022-04-27 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0008_remove_app_cost_app_cost_monthely_app_cost_yearly'),
    ]

    operations = [
        migrations.AddField(
            model_name='appgroup',
            name='importance',
            field=models.PositiveIntegerField(default=4, verbose_name='importance'),
            preserve_default=False,
        ),
    ]
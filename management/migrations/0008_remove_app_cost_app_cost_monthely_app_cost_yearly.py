# Generated by Django 4.0.3 on 2022-04-27 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0007_alter_app_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='app',
            name='cost',
        ),
        migrations.AddField(
            model_name='app',
            name='cost_monthely',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='cost monthely'),
        ),
        migrations.AddField(
            model_name='app',
            name='cost_yearly',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='cost yearly'),
        ),
    ]

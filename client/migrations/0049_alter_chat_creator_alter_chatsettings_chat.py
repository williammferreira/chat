# Generated by Django 4.0.3 on 2022-05-17 23:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('client', '0048_chatsettings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creator_of', to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.AlterField(
            model_name='chatsettings',
            name='chat',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='settings', to='client.chat', verbose_name='Chat'),
        ),
    ]

# Generated by Django 4.0.3 on 2022-05-06 18:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('client', '0015_alter_profile_theme'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chats',
            name='locationUrl',
        ),
        migrations.RemoveField(
            model_name='chats',
            name='token',
        ),
        migrations.AddField(
            model_name='chats',
            name='id',
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chats',
            name='chatCreator',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL,
                                       related_name='chatCreator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='chats',
            name='chatDateCreated',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='chats',
            name='chatDescription',
            field=models.CharField(max_length=100),
        ),
        migrations.RemoveField(
            model_name='chats',
            name='chatUsers',
        ),
        migrations.AddField(
            model_name='chats',
            name='chatUsers',
            field=models.ManyToManyField(
                related_name='chatUsers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='theme',
            field=models.CharField(choices=[('dark', 'Dark'), ('bluelines', 'Blue_Lines'), (
                'light', 'Light')], default='black', max_length=10),
        ),
    ]

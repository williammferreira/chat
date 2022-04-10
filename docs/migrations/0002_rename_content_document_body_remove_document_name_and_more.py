# Generated by Django 4.0.3 on 2022-03-26 22:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='content',
            new_name='body',
        ),
        migrations.RemoveField(
            model_name='document',
            name='name',
        ),
        migrations.RemoveField(
            model_name='group',
            name='name',
        ),
        migrations.AddField(
            model_name='document',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='document',
            name='status',
            field=models.CharField(choices=[('published', 'Published'), ('draft', 'Draft')], default='draft', max_length=50),
        ),
        migrations.AddField(
            model_name='document',
            name='title',
            field=models.CharField(default='sdasd', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='group',
            name='title',
            field=models.CharField(default='sdf', max_length=50),
            preserve_default=False,
        ),
    ]

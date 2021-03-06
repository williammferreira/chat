# Generated by Django 4.0.3 on 2022-03-26 23:06

from django.db import migrations, models
import django.db.models.deletion
import docs.models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0006_alter_group_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='group',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='document_children', to='docs.group'),
        ),
        migrations.AlterField(
            model_name='group',
            name='id',
            field=models.CharField(default=docs.models.Group.get_UUID4_hex, editable=False, max_length=1000, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='group',
            name='parent',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='group_children', to='docs.group'),
        ),
    ]

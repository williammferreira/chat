# Generated by Django 4.0.3 on 2022-03-26 22:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0005_alter_document_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='id',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=1000, primary_key=True, serialize=False),
        ),
    ]

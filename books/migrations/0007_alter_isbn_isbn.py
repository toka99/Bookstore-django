# Generated by Django 3.2 on 2021-04-22 11:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_alter_isbn_isbn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='isbn',
            name='isbn',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]

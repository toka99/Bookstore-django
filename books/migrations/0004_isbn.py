# Generated by Django 3.2 on 2021-04-22 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20210422_1155'),
    ]

    operations = [
        migrations.CreateModel(
            name='Isbn',
            fields=[
                ('isbn', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
            ],
        ),
    ]
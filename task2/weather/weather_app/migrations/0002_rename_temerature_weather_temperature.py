# Generated by Django 5.1 on 2024-12-11 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weather',
            old_name='temerature',
            new_name='temperature',
        ),
    ]

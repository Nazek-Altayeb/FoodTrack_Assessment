# Generated by Django 5.0 on 2023-12-19 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_rename_time_openinghours_open_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='state',
            new_name='street',
        ),
    ]

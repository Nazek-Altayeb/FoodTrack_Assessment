# Generated by Django 5.0 on 2023-12-18 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_openinghours_branch'),
    ]

    operations = [
        migrations.RenameField(
            model_name='openinghours',
            old_name='time',
            new_name='open_at',
        ),
    ]

# Generated by Django 5.0 on 2023-12-14 18:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_store_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='address',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='store.address'),
        ),
    ]

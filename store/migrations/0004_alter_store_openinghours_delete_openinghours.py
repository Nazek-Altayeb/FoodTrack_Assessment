# Generated by Django 5.0 on 2023-12-13 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_store_openinghours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='openingHours',
            field=models.CharField(choices=[('00:06', '00:06 AM'), ('00:09', '00:09 AM'), ('00:12', '00:12 PM')], max_length=200),
        ),
        migrations.DeleteModel(
            name='OpeningHours',
        ),
    ]

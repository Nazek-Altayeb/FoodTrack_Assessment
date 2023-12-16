# Generated by Django 5.0 on 2023-12-16 16:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_store_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodName', models.CharField(default='not-specified', max_length=100)),
                ('salesPerDay', models.IntegerField()),
                ('returnedItemsPerDay', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OpeningHours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=100)),
                ('time', models.TimeField()),
            ],
        ),
        migrations.AddField(
            model_name='store',
            name='food',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='food', to='store.food'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='store',
            name='openingHours',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='openingHours', to='store.openinghours'),
        ),
    ]

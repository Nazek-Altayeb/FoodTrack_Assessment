# Generated by Django 5.0 on 2023-12-17 17:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_food_openinghours_store_food_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='food',
        ),
        migrations.RemoveField(
            model_name='store',
            name='openingHours',
        ),
        migrations.AddField(
            model_name='openinghours',
            name='store',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='openingHours', to='store.store'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Foods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodName', models.CharField(default='not-specified', max_length=100)),
                ('salesPerDay', models.IntegerField()),
                ('returnedItemsPerDay', models.IntegerField()),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foods', to='store.store')),
            ],
        ),
        migrations.DeleteModel(
            name='Food',
        ),
    ]

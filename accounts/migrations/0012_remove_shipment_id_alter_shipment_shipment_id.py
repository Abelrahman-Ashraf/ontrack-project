# Generated by Django 4.2.6 on 2024-06-23 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_rename_reserved_date_shipment_received_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipment',
            name='id',
        ),
        migrations.AlterField(
            model_name='shipment',
            name='shipment_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

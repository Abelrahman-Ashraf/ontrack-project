# Generated by Django 4.2.6 on 2024-06-23 10:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0009_shipment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='about_shipment',
            field=models.TextField(blank=True, verbose_name='about'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='last_location',
            field=models.CharField(max_length=200, verbose_name='last location'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='receiver_name',
            field=models.CharField(max_length=200, verbose_name='receiver name'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='receiver_phone',
            field=models.CharField(max_length=20, verbose_name='reciever phone'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='reserved_date',
            field=models.DateField(blank=True, null=True, verbose_name='resieved date'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='sender_name',
            field=models.CharField(max_length=200, verbose_name='sender name'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='sender_phone',
            field=models.CharField(max_length=20, verbose_name='sender phone'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='sent_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='shipment_id',
            field=models.CharField(max_length=50, unique=True, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='shipment_type',
            field=models.CharField(max_length=100, verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='shipment_weight',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='wieght'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='start_location',
            field=models.CharField(max_length=200, verbose_name='start location'),
        ),
    ]
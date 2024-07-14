# Generated by Django 4.2.6 on 2024-06-23 10:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0008_remove_profile_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipment_id', models.CharField(max_length=50, unique=True)),
                ('shipment_type', models.CharField(max_length=100)),
                ('shipment_weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('receiver_name', models.CharField(max_length=200)),
                ('sender_name', models.CharField(max_length=200)),
                ('sender_phone', models.CharField(max_length=20)),
                ('receiver_phone', models.CharField(max_length=20)),
                ('start_location', models.CharField(max_length=200)),
                ('last_location', models.CharField(max_length=200)),
                ('reserved_date', models.DateField(blank=True, null=True)),
                ('about_shipment', models.TextField(blank=True)),
                ('sent_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'shipment',
                'verbose_name_plural': 'shipments',
            },
        ),
    ]

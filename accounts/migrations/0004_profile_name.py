# Generated by Django 4.2.6 on 2024-03-30 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_name_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default='anything', max_length=50, verbose_name='name'),
        ),
    ]

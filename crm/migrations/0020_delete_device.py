# Generated by Django 3.0.3 on 2020-09-13 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0019_remove_sendwa_device'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Device',
        ),
    ]

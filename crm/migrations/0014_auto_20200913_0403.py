# Generated by Django 3.0.3 on 2020-09-13 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0013_auto_20200913_0401'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sendwa',
            old_name='choices',
            new_name='type_message',
        ),
    ]

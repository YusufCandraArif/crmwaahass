# Generated by Django 3.0.3 on 2020-09-13 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0018_auto_20200913_0606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sendwa',
            name='device',
        ),
    ]

# Generated by Django 3.0.3 on 2020-09-13 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0016_auto_20200913_0602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sendwa',
            name='device',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='device', to='crm.Device'),
        ),
    ]

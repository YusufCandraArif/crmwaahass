# Generated by Django 3.0.3 on 2020-08-26 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_auto_20200826_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date_h3',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='date_h7',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='date_phone',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]

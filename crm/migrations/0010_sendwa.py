# Generated by Django 3.0.3 on 2020-09-13 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0009_auto_20200912_0911'),
    ]

    operations = [
        migrations.CreateModel(
            name='SendWA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='images/')),
                ('media_url', models.URLField(blank=True, default='', max_length=450, null=True)),
                ('document', models.FileField(blank=True, default='', null=True, upload_to='document/')),
                ('choices', models.CharField(choices=[('Text Only', 'Text Only'), ('Image Text', 'Image Text'), ('Video', 'Video'), ('Document', 'Document')], default='', max_length=200)),
                ('location', models.CharField(blank=True, choices=[('', ''), ('Jawa Tengah', 'Jawa Tengah'), ('Jawa Timur', 'Jawa Timur'), ('Jawa Barat', 'Jawa Barat'), ('Banten', 'Banten'), ('DKI Jakarta', 'DKI Jakarta'), ('Yogyakarta', 'Yogyakarta')], default='', max_length=200, null=True)),
                ('strdate', models.CharField(default='2020-09-13', max_length=40)),
                ('count', models.IntegerField(blank=True)),
                ('scheduled', models.CharField(blank=True, choices=[('24', '1 DAY')], default='', max_length=200, null=True)),
            ],
        ),
    ]

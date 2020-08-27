import threading
from django.db import models
from PIL import Image
from datetime import datetime, timedelta
from django.utils import timezone

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True, blank=False)
    no_motor = models.CharField(max_length=200, null=True, blank=False)
    phone = models.CharField(max_length=200, null=True, blank=False)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(null=True)
    date_h7 = models.DateTimeField(null=True)
    date_h3 = models.DateTimeField(null=True)
    date_phone = models.DateTimeField(null=True)
    status_h7 = models.BooleanField(default=False)
    status_h3 = models.BooleanField(default=False)
    status_telpon = models.BooleanField(default=False)
    status_whatsapp = models.BooleanField(default=False)
    status_kedatangan = models.BooleanField(default=False)
    status_call = models.BooleanField(default=False)
    tipe_motor = models.CharField(max_length=200, null=True, blank=False)
    km_akhir = models.CharField(max_length=200, null=True, blank=False)
    ket = models.CharField(max_length=200, null=True, blank=False)

    def save(self, *args, **kwargs):
        date_time = datetime.now()
        self.date_created = date_time.strftime('%Y-%m-%d %H:%M:%S')
        self.date_h7 = date_time + timedelta(days=53)
        self.date_h3 = date_time + timedelta(days=57)
        self.date_phone = date_time + timedelta(days=59)
        super(Customer, self).save(*args, **kwargs)

    
    def __str__(self):
        return self.name


    #         # cr_date = datetime.strptime(sale.write_date, '%Y-%m-%d %H:%M:%S')
    #         # tanggal_h7 = cr_date + timedelta(days=53)
    #         # tanggal_h3 = cr_date + timedelta(days=57)
    #         # tanggal_telpon = cr_date + timedelta(days=59)
import hashlib
from django.db import models
from PIL import Image
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib.auth.models import User
from ahass import settings
from .apiwa import send_whatsapp

class Token(models.Model):
    SECRET_KEY = settings.SECRET_KEY

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mytoken = models.CharField(max_length=500, blank=True, default='')
    # token_email = models.CharField(max_length=500, blank=True)
    # token_user = models.CharField(max_length=500, blank=True)

    def save(self, *args, **kwargs):
        source_token = self.SECRET_KEY + self.user.username + self.user.email
        hash_token = hashlib.md5(source_token.encode()).hexdigest()
        self.mytoken = hash_token
        super(Token, self).save(*args, **kwargs) 

    def __str__(self):
        return '{} - {}'.format(self.user.username, self.user.email)

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True, blank=False)
    no_motor = models.CharField(max_length=200, null=True, blank=False)
    phone = models.CharField(max_length=200, null=True, blank=False)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_h7 = models.DateTimeField(auto_now_add=True, null=True)
    date_h3 = models.DateTimeField(auto_now_add=True, null=True)
    date_phone = models.DateTimeField(auto_now_add=True, null=True)
    status_h7 = models.BooleanField(default=False)
    status_h3 = models.BooleanField(default=False)
    status_telpon = models.BooleanField(default=False)
    status_whatsapp = models.BooleanField(default=False)
    status_kedatangan = models.BooleanField(default=False)
    status_call = models.BooleanField(default=False)
    tipe_motor = models.CharField(max_length=200, null=True, blank=False)
    km_akhir = models.CharField(max_length=200, null=True, blank=False)
    ket = models.CharField(max_length=200, null=True, blank=False)
    message1 = models.TextField(default='', blank=True)
    message2 = models.TextField(default='', blank=True)
    message3 = models.TextField(default='', blank=True)
    message4 = models.TextField(default='', blank=True)
    status_message1 = models.BooleanField(default=False)
    status_message2 = models.BooleanField(default=False)
    status_message3 = models.BooleanField(default=False)
    status_message4 = models.BooleanField(default=False)
    
    def __str__(self):
        return 'Customer: {}'.format(self.name)


class Device(models.Model):
    phone = models.CharField(max_length=200, null=True, blank=False)
    device_code = models.CharField(max_length=200, null=True, blank=False)
    token_api = models.CharField(max_length=300, null=True, blank=False)
    server_address = models.CharField(max_length=200, null=True, blank=False, help_text="Only main name server address. Example: wa.test.com")
    location = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return 'Device: {}'.format(self.phone)

class SendWA(models.Model):
    CHOICES = (
			('Text Only', 'Text Only'),
			('Image', 'Image'),
			('Video', 'Video'),
			('Document','Document'),
			)
    
    LOCATION = (
			('',''),
			('Jawa Tengah', 'Jawa Tengah'),
			('Jawa Timur', 'Jawa Timur'),
			('Jawa Barat','Jawa Barat'),
			('Banten','Banten'),
			('DKI Jakarta','DKI Jakarta'),
			('Yogyakarta','Yogyakarta')
			)
        
    MESSAGES = (
			('Message 1', 'Message 1'),
			('Message 2', 'Message 2'),
			('Message 3', 'Message 3'),
			('Message 4','Message 4'),
			)
    
    messages = models.CharField(max_length=200, default='', null=False, choices=MESSAGES)
    message = models.TextField(null=False, blank=True)
    media_url = models.URLField(max_length=450, default='', null=True, blank=True)
    type_media_url = models.CharField(max_length=200, default='', null=False, choices=CHOICES)
    location = models.CharField(max_length=200, default='',blank=True, null=True, choices=LOCATION)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, default='', related_name="device", null=True, blank=True)
    
    def __str__(self):
        return "Sendwa: {}".format(self.created_at)

    def save(self, *args, **kwargs):
        custmers = Customer.objects.all()
        for customer in custmers:
            phone = customer.phone
            if phone:
                status = send_whatsapp(self.message, self.media_url,
                                        self.type_media_url, phone,
                                        self.device.token_api,
                                        self.device.server_address)
                if self.messages == 'Message 1':
                    customer.message1 = self.message
                    customer.status_message1 = status
                    customer.save()
                elif self.messages == 'Message 2':
                    customer.message2 = self.message
                    customer.status_message2 = status
                    customer.save()
                elif self.messages == 'Message 3':
                    customer.message3 = self.message
                    customer.status_message3 = status
                    customer.save()
                elif self.messages == 'Message 4':
                    customer.message4 = self.message
                    customer.status_message4 = status
                    customer.save()

        super(SendWA, self).save(*args, **kwargs) 
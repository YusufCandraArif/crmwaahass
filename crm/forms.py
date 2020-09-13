from django.forms import ModelForm
from .models import Customer, SendWA, Device
from django.core.validators import validate_email
from django import forms
import phonenumbers
from datetime import datetime
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = ['name', 'no_motor', 'phone', 'email', 'tipe_motor','km_akhir']
	
	def clean(self):
		data = self.cleaned_data

		z = phonenumbers.parse(data.get("phone"), "ID")
		if not phonenumbers.is_valid_number(z):
			raise forms.ValidationError("Invalid phone number")

class SendwaForm(ModelForm):
	class Meta:
		model = SendWA
		fields = ['messages',
				'type_media_url',
				'device', 
				'message',
				# 'image',
				# 'document',
				'media_url',
				'location',]

	def clean(self):
		data = self.cleaned_data
		messages = data.get('messages')
		message = data.get('message')
		media_url = data.get('media_url')		
		device = data.get('device')
		# document = data.get('document')
		# type_media_url = data.get('type_media_url')		
		
		if not messages:
			raise forms.ValidationError("Messages cannot be blank.")
			
		if not message and not media_url:
			raise forms.ValidationError("Invalid send message value.")

		if not device:
			raise forms.ValidationError("Please choose the device.")			


class CreateDeviceForm(ModelForm):
	class Meta:
		model = Device
		fields = [
			"phone",
			"device_code", 
			"token_api", 
			"server_address", 
			"location",
			] 

	def clean(self):
		data = self.cleaned_data
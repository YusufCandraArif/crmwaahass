from django.forms import ModelForm
from .models import Customer
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

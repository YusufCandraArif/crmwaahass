from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .models import *
from .resources import CustomerResource
from .forms import CustomerForm, CreateUserForm, SendwaForm, CreateDeviceForm
from crm.models import Customer, Device
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from tablib import Dataset
from io import BytesIO
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa


def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'accounts/register.html', context)

def loginPage(request):
	token = Token.objects.filter(user__username=request.POST.get('username'),
								mytoken=request.POST.get('token'))
	if request.method == 'POST' and not token and request.POST.get('username') != 'admin' :
		data = {
			"username": request.POST.get('username'),
			"mytoken": request.POST.get('token')
		}
		context = {'token':data}
		return render(request, 'accounts/error_token.html', context)

	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def home(request):
	customers = Customer.objects.all()
	total_customers = customers.count()
	device = Device.objects.all()

	context = {'customers':customers,
		'total_customers':total_customers,
		'devices': device,
		}

	return render(request, 'accounts/dashboard.html', context)

def createCustomer(request):
	form = CustomerForm()
	if request.method == 'POST':
		new_persons = request.FILES['myfile']
		if new_persons:
			person_resource = CustomerResource()
			dataset = Dataset()
			imported_data = dataset.load(new_persons.read().decode('utf-8'), format='csv')
			result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

			if not result.has_errors():
				person_resource.import_data(dataset, dry_run=False)  # Actually import now
			return redirect('/')

		form = CustomerForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'accounts/customer_form.html', context)

def updateCustomer(request, pk):
	customer = Customer.objects.get(id=pk)
	form = CustomerForm(instance=customer)

	if request.method == 'POST':
		form = CustomerForm(request.POST, instance=customer)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'accounts/customer_update.html', context)

def deleteCustomer(request, pk):
	user = Customer.objects.get(id=pk)
	if request.method == "POST":
		user.delete()
		return redirect('/')

	context = {'item':user}
	return render(request, 'accounts/delete_customer.html', context)


def customer(request, pk_test):
	customer = Customer.objects.get(id=pk_test)


	context = {'customer':customer}
	return render(request, 'accounts/customer.html',context)

def customers(request):
	customers = Customer.objects.all()

	context= {'customers':customers}
	return render(request, 'accounts/customers.html', context)

def devices(request):
	devices = Device.objects.all()

	context= {'devices':devices}
	return render(request, 'accounts/devices.html', context)

# def sendwa(request):
# 	form = SendwaForm()
# 	phones = Customer.objects.all().values_list("phone")
# 	if request.method == 'POST':
# 		form = SendwaForm(request.POST, request.FILES)
# 		if form.is_valid():
# 			form.save()
# 			cur_sender = SendWA.objects.latest('id')
# 			location = ''
# 			if request.POST.get('location'):
# 				location = request.POST.get('location')
# 				object_phones = Customer.objects.filter(location=location)
# 				if object_phones:
# 					phones = [(phone.phone,) for phone in object_phones]

# 			cur_sender.blaster(phones)
			
# 			return redirect('/')
	
# 	context = {"form": form}
# 	return render(request, 'accounts/sendwa_form.html', context)


##### SEND WHATSAPP #####
def sendwa(request):
	form = SendwaForm()
	if request.method == 'POST':
		form = SendwaForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
	
			return redirect('/')
	
	context = {"form": form}
	return render(request, 'accounts/sendwa_form.html', context)


##### ADD DEVICE #####
def create_device(request):
	form = CreateDeviceForm()
	if request.method == 'POST':
		form = CreateDeviceForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	
	context = {"form": form}
	return render(request, 'accounts/device_form.html', context)



##### PDF VIEW & DOWNLOAD #####
def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None


#Opens up page as PDF
class ViewPDF(View):
	def get(self, request, *args, **kwargs):
		data = {
			"company": "Nama Perusahaan",
			"address": "Alamat Perusahaan",
			"city": "Yogyakarta",
			"state": "Indonesia",
			"zipcode": "98663",


			"phone": "085643147350",
			"email": "cancanunyu@gmail.com",
			"website": "https://github.com/YusufCandraArif",
			}
		pdf = render_to_pdf('accounts/pdf_template.html', data)
		return HttpResponse(pdf, content_type='application/pdf')


#Automaticly downloads to PDF file
class DownloadPDF(View):
	def get(self, request, *args, **kwargs):
		data = {
			"company": "Nama Perusahaan",
			"address": "Alamat Perusahaan",
			"city": "Yogyakarta",
			"state": "Indonesia",
			"zipcode": "98663",


			"phone": "085643147350",
			"email": "cancanunyu@gmail.com",
			"website": "https://github.com/YusufCandraArif",
			}		
		pdf = render_to_pdf('accounts/pdf_template.html', data)

		response = HttpResponse(pdf, content_type='application/pdf')
		filename = "Invoice_%s.pdf" %("12341231")
		content = "attachment; filename='%s'" %(filename)
		response['Content-Disposition'] = content
		return response

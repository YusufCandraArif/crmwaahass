from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .models import *
from .resources import CustomerResource
from .forms import CustomerForm, CreateUserForm
from crm.models import Customer
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from tablib import Dataset

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

	context = {'customers':customers,
	'total_customers':total_customers}

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
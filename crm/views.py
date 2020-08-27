from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .models import *
from .forms import CustomerForm
from crm.models import Customer

def home(request):
	customers = Customer.objects.all()
	total_customers = customers.count()

	context = {'customers':customers,
	'total_customers':total_customers}

	return render(request, 'accounts/dashboard.html', context)

def createCustomer(request):
	form = CustomerForm()
	if request.method == 'POST':
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
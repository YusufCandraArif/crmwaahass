from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('customers/', views.customers, name='customers'),
    path('customer/<str:pk_test>/', views.customer, name="customer"),
    path('create_customer/', views.createCustomer, name="create_customer"),
    path('update_customer/<str:pk>/', views.updateCustomer, name="update_customer"),
    path('delete_customer/<str:pk>/', views.deleteCustomer, name="delete_customer"), 
    
]
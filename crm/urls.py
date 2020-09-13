from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('customers/', views.customers, name='customers'),
    path('customer/<str:pk_test>/', views.customer, name="customer"),
    path('create_customer/', views.createCustomer, name="create_customer"),
    path('update_customer/<str:pk>/', views.updateCustomer, name="update_customer"),
    path('delete_customer/<str:pk>/', views.deleteCustomer, name="delete_customer"), 
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),

    path('sendwa/', views.sendwa, name="send_wa"),

    path('pdf_view/', views.ViewPDF.as_view(), name="pdf_view"),
    path('pdf_download/', views.DownloadPDF.as_view(), name="pdf_download"),

    path('create_device/', views.create_device, name="create_device"),
    path('devices/', views.devices, name='devices'),
]

from django.contrib import admin
from django.urls import path
from careapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('index', views.index ,name="index"),

    path('starter/', views.starter,name="starter"),

    path('about/', views.about,name="about"),

    path('services/', views.services,name="services"),

    path('appointment/', views.appoint,name="appointment"),

    path('departments/', views.departments,name="departments"),

    path('show/', views.show,name="show"),

    path('delete/<int:id>', views.delete),

    path('edit/<int:id>', views.edit),

    path('', views.register,name="register"),

    path('login/', views.login_user,name="login"),

    #Mpesa URLS

   #Mpesa URLS
    path('pay/', views.pay, name='pay'),

    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),
    path('payment-result/', views.payment_result, name='payment_result'),
    path('transactions/', views.transactions_list, name='transactions'),


]

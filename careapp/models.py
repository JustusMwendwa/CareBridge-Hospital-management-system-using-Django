from django.db import models

# Create your models here.
class Patient(models.Model):
    firstname =models.CharField(max_length=20)
    surname =models.CharField(max_length=20)
    age =models.IntegerField()
    dob =models.DateField()
    phone =models.CharField(max_length=10)
    visitdate =models.DateTimeField()
    medicalhistory=models.TextField()


    def __str__(self):
        return self.firstname + " " + self.surname



class MedicalRecords(models.Model):
    patientname =models.CharField(max_length=20)
    doctor =models.CharField(max_length=50)
    diagnosis =models.TextField()
    email =models.EmailField()

    def __str__(self):
        return self.patientname

class Appointments(models.Model):
    name =models.CharField(max_length=20)
    email =models.EmailField()
    phone =models.CharField(max_length=10)
    datetime =models.DateTimeField()
    department =models.CharField(max_length=50)
    doctor =models.CharField(max_length=50)
    message =models.TextField()


    def __str__(self):
        return self.name
    

class Transaction(models.Model):
    phone_number = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20, choices=[('Success', 'Success'), ('Failed', 'Failed')])
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.phone_number} - {self.amount} - {self.status}"
from django.db import models

# Create your models here.
class Details(models.Model):
    student_name=models.CharField(max_length=50)
    father_name=models.CharField(max_length=50)
    Dob=models.DateField(max_length=20)
    Address=models.CharField(max_length=100)
    City=models.CharField(max_length=50)
    State=models.CharField(max_length=40)
    Pin=models.IntegerField(max_length=10)
    PhoneNo=models.IntegerField(max_length=10,unique=True)
    Email=models.EmailField(max_length=50)
    Class=models.IntegerField(max_length=2)
    Date_Enrolled=models.DateTimeField()
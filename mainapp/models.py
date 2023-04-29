from distutils.command.upload import upload
from email.mime import image
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.


class UserProfile(models.Model):
    username = models.OneToOneField(User, on_delete=CASCADE)
    email = models.EmailField()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    addres = models.CharField(max_length=60)
    city = models.CharField(max_length=60) 
    country = models.CharField(max_length=60)
    postal_code = models.CharField(max_length=60)  
    about = models.TextField()
    avatar = models.ImageField(upload_to='profile')
    
    def __str__(self):
        return str(self.username)
    
class Employee(models.Model):
    full_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    country = models.CharField(max_length=70)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=70)
    image = models.ImageField(upload_to='employee')
    salary = models.FloatField()
    
    def __str__(self):
        return self.full_name
    
    
    def final_salary(self):
        one_per = self.salary / 100
        ten_per = one_per * 10
        final_salary = self.salary - ten_per 
        return final_salary
        
    
class Product(models.Model):
    title = models.CharField(max_length=100)
    create_date = models.DateField()
    end_date = models.DateField()
    quontity = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='product')
    price = models.FloatField()
    # total_price = models.FloatField()
    
    def __str__(self):
        return self.title
    
    def total_amounts(self):
        total_amounts = self.price * self.quontity
        return total_amounts 
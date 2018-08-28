from django.db import models

# Create your models here.
class contact(models.Model):
    Name =models.CharField(max_length =100)
    Email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=30)
    Age=models.CharField(max_length=10,default='', blank=True)
    Gender=models.CharField(max_length=50,default='', blank=True)
    comment=models.TextField(default='', blank=True)
    
    
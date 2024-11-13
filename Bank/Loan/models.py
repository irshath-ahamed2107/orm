from django.db import models 
from django.contrib import admin 
class Loan_DB(models.Model): 
    Customer_ID=models.CharField(max_length=20, primary_key=True) 
    Customer_name=models.CharField(max_length=100) 
    Loan_no=models.IntegerField() 
    Loan_amount=models.IntegerField() 
    Mail_ID=models.EmailField() 
class Loan_DBAdmin(admin.ModelAdmin): 
    list_display=('Customer_ID','Customer_name','Loan_no','Loan_amount','Mail_ID')
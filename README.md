# Ex02 Django ORM Web Application
## Date: 30.10.24

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
admin.py
```
from django.contrib import admin 
from .models import Loan_DB, Loan_DBAdmin 
admin.site.register(Loan_DB, Loan_DBAdmin) 
```

models.py

```
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
```



## OUTPUT
 
 ![Screenshot 2024-11-13 142301](https://github.com/user-attachments/assets/1417bfc2-6763-434e-ac85-757190157bf8)



## RESULT
Thus the program for creating a database using ORM hass been executed successfully

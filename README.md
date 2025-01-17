# Ex02 Django ORM Web Application
## Date: 28/02/2024

## AIM
To develop a Django application to store and retrieve data from a Book database using Object Relational Mapping(ORM).

## Entity Relationship Diagram

![alt text](ER.jpg)

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

```
admin.py

from django.contrib import admin
from.models import Book_DB,Book_DBAdmin
admin.site.register(Book_DB,Book_DBAdmin)

model.py

from django.db import models
from django.contrib import admin
class Book_DB(models.Model):
    b_id = models.IntegerField(primary_key="b_id");
    b_name = models.CharField(max_length=100);
    b_author = models.CharField(max_length=100);
    b_edition = models.CharField(max_length=20);
    b_year = models.DateField();

class Book_DBAdmin(admin.ModelAdmin):
    list_display = ("b_id","b_name","b_author","b_edition","b_year");

```

## OUTPUT

![Screenshot 2024-03-13 104326](https://github.com/jayahari10001/ORM/assets/115681467/248d896c-90e5-4345-add3-eb6116a0b22c)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully

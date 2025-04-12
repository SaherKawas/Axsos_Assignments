from django.db import models

class User(models.Model): #this is not a normal class, this is a class that inherit from models.Model and that will be reflected in the database(it will put it in the database)
    name= models.CharField(max_length=30)        # we want to define the columns in the database/ charfield is equivalent to varchar
    phonenumber= models.CharField(max_length=14)
    address= models.TextField()
    created_at=models.DateTimeField(auto_now_add=True) #django will reflect it in the database when you create a row
    updated_at=models.DateTimeField(auto_now=True)

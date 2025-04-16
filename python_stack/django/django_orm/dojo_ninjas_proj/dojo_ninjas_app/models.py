from django.db import models

class Dojo(models.Model):
    name=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    created_at=models.DateTimeField(auto_now_add=True) #django will reflect it in the database when you create a row
    updated_at=models.DateTimeField(auto_now=True)
    desc=models.TextField()

class Ninja(models.Model):
    dojo=models.ForeignKey(Dojo, related_name="ninjas", on_delete=models.CASCADE) 
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    created_at=models.DateTimeField(auto_now_add=True) #django will reflect it in the database when you create a row
    updated_at=models.DateTimeField(auto_now=True)

def create_dojo(post):
    return Dojo.objects.create(name=post["name"], city=post['city'], state=post['state'])

def create_ninja(post):
    dojo= Dojo.objects.get(id=post['location'])

    Ninja.objects.create(first_name=post['firstname'], last_name=post['lastname'], dojo=dojo)
from django.db import models

class User(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    age=models.IntegerField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

def create_user(post):
    return User.objects.create(firstname=post["firstname"], lastname=post['lastname'], email=post['email'], age=post['age'])
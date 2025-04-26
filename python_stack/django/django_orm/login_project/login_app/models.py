from django.db import models
import re
import bcrypt

class LoginManager(models.Manager):
    def register_validator(self, post):
        errors={}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        
        if len(post['firstname'])<2:
            errors['firstname']="First Name should be at least two characters"
        if len(post['lastname'])<2:
            errors['lastname']="Last Name should be at least two characters"
        if not EMAIL_REGEX.match(post['email']):
            errors['email'] = "Invalid email address!"
        if len(post['password'])<8:
            errors['password']="Password should be at least 8 characters"
        
        return errors


class Login(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True) 
    updated_at=models.DateTimeField(auto_now=True)
    objects = LoginManager()

def create_user(post):
    return Login.objects.create(firstname=post['firstname'], lastname=post['lastname'], email=post['email'], password=post['password'])

def log_check(post):
    email=post['email']
    password=post['password']
    user=Login.objects.get(email=email)
    if bcrypt.checkpw(password.encode(), user.password.encode()):
        print('password match')
        return True
    else:
        print('password mismatch')
    hash1 = bcrypt.hashpw('password'.encode(), bcrypt.gensalt()).decode()
    print(hash1)
    return False

def getuser(email):
    return Login.objects.get(email=email)
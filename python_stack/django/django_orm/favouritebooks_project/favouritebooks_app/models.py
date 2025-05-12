from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
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
    
class BookManager(models.Manager):
    def book_validator(self, post):
        errors={}

        if 'title' not in post or len(post['title']) == 0:
            errors['title']="Title is required!"
        if len(post['description'])<5:
            errors['description']="Description should be at least 5 characters"

        return errors


class User(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True) 
    updated_at=models.DateTimeField(auto_now=True)
    objects = UserManager()

class Book(models.Model):
    title=models.CharField(max_length=255)
    desc=models.CharField(max_length=255)
    uploaded_by=models.ForeignKey(User, related_name='books_uploaded', on_delete = models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True) 
    updated_at=models.DateTimeField(auto_now=True)
    objects=BookManager()

def create_user(post):
    return User.objects.create(firstname=post['firstname'], lastname=post['lastname'], email=post['email'], password=post['password'])

def log_check(post):
    email=post['email']
    password=post['password']
    user=User.objects.get(email=email)
    if bcrypt.checkpw(password.encode(), user.password.encode()):
        print('password match')
        return True
    else:
        print('password mismatch')
    hash1 = bcrypt.hashpw('password'.encode(), bcrypt.gensalt()).decode()
    print(hash1)
    return False

def getuser(email):
    return User.objects.get(email=email)

def create_book(post, userid):
    user = User.objects.get(id=userid)
    return Book.objects.create(title=post['title'], desc=post['description'], uploaded_by=user)

def allbooks():
    return Book.objects.all() 
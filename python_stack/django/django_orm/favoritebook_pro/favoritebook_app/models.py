from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def basic_validator(self, post):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(post['firstname']) < 2:
            errors["firstname"] = "First name should be at least 2 characters"
        if len(post['lastname']) < 2:
            errors["lastname"] = "Last name should be at least 2 characters"
        if not EMAIL_REGEX.match(post['email']):               
            errors['email'] = "Invalid email address!"
        if len(post['password'])<8:
            errors['password']="Password should be at least 8 characters"
        return errors
        


class User(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects=UserManager()


class Book(models.Model):
    title=models.CharField(max_length=255)
    desc=models.CharField(max_length=255)
    uploaded_by= models.ForeignKey(User, related_name="booksapploaded", on_delete = models.CASCADE)
    users_who_like=models.ForeignKey(User, related_name="booksliked", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

def create_user(post):
    return User.objects.create(firstname=post['firstname'], lastname=post['lastname'], email=post['email'], password=post['password'])

def log_check(post):
    email=post['email']
    password=post['password']
    user = User.objects.filter(email=email).first()
    if not user:
        print('user not found')
        return False
    if bcrypt.checkpw(password.encode(), user.password.encode()):
        print('password match')
        return True
    else:
        print('password mismatch')
    return False

def getuser(email):
    return User.objects.get(email=email)
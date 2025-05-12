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
    
    def login_validator(self, post):
        errors={}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        
        if not EMAIL_REGEX.match(post['email']):
            errors['email'] = "Invalid email address!"
        if len(post['password'])<8:
            errors['password']="Password should be at least 8 characters"

        return errors

class ProjectManager(models.Manager):
    def project_validator(self, post):
        errors={}

        if len(post['projectname'])<3:
            errors['projectname']="Project Name should be at least 3 characters"

        if len(post['description'])<10:
            errors['description']="Description should be at least 10 characters"

class User(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True) 
    updated_at=models.DateTimeField(auto_now=True)
    objects = UserManager()

class Project(models.Model):
    name=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    start_date=models.DateField()
    end_date=models.DateField()
    user=models.ForeignKey(User, related_name='projects', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True) 
    updated_at=models.DateTimeField(auto_now=True)
    objects=ProjectManager()


def create_user(post):
    return User.objects.create(firstname=post['firstname'], lastname=post['lastname'], email=post['email'], password=post['password'])

def getuser(email):
    return User.objects.get(email=email)

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

def get_user(id):
    return User.objects.get(id=id)

def create_project(post):
    return Project.objects.create(name=post['projectname'], description=post['description'], start_date=post['startdate'], end_date=post['enddate'])
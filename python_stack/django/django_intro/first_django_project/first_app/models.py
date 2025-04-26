from django.db import models
import re
import bcrypt

class UserManager(models.Manager): #this is a validation for the User class. if I want to validate the address class, then I should create a an AddressManager class.
    def reg_validator(self, post):
        errors={}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(post['name'])==0:
            errors['user_name']="Name is required"
        if len(post['name'])<9:
            errors['name_length']="Name must be more than 9"
        if len('phonenumber')==0:
            errors['phonenumber']="phonenumber is required"
        if len('phonenumber')!=10:
            errors['phonenumber_length']="phone number must be 10 digits"
        return errors
    
    # def login_validator(self, loginform):


class User(models.Model): #this is not a normal class, this is a class that inherit from models.Model and that will be reflected in the database(it will put it in the database)
    name= models.CharField(max_length=30)        # we want to define the columns in the database/ charfield is equivalent to varchar
    phonenumber= models.CharField(max_length=14)
    password=models.CharField(max_length=255) #we add password to the class
    created_at=models.DateTimeField(auto_now_add=True) #django will reflect it in the database when you create a row
    updated_at=models.DateTimeField(auto_now=True)
    #addresses: i can get the address using reveresd lookup
    objects=UserManager()

class Address(models.Model):
    country=models.CharField(max_length=30) 
    city=models.CharField(max_length=30) 
    street=models.CharField(max_length=100) 
    user=models.ForeignKey(User, related_name="addresses", on_delete=models.CASCADE) #or do nothing if i don't want to delete the addresses of the user.
    created_at=models.DateTimeField(auto_now_add=True) #django will reflect it in the database when you create a row
    updated_at=models.DateTimeField(auto_now=True)

def get_all_users():
    return User.objects.all()

def get_user (id):
    return User.objects.get(id=id)

def create_user(post):
    return User.objects.create(name=post["name"], phonenumber=post['phonenumber'], address=post['address'])
def delete_user_from_DB(id):
    my_user= User.objects.get(id=id)
    my_user.delete()

def test_many_to_many(book id, publisher_id):
    mybook=Book.objects. get(id=book_id)
    mypublisher=Publisher.object.get(id=publisher_id)

    mybook.publishers.add(mypublisher) #is the same as mypublisher.books.add(mybook)
    
def log_check(postdata):
    name=postdata['name']
    password=postdata['password']
    user=User.objects.get(name=name)
    if bcrypt.checkpw(password.encode(), user.password.encode()):
        print('password match')
    else:
        print('password mismatch')
    hash1 = bcrypt.hashpw('password'.encode(), bcrypt.gensalt()).decode()
    print(hash1)
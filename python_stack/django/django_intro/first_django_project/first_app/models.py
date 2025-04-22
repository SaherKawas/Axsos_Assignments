from django.db import models

class User(models.Model): #this is not a normal class, this is a class that inherit from models.Model and that will be reflected in the database(it will put it in the database)
    name= models.CharField(max_length=30)        # we want to define the columns in the database/ charfield is equivalent to varchar
    phonenumber= models.CharField(max_length=14)
    created_at=models.DateTimeField(auto_now_add=True) #django will reflect it in the database when you create a row
    updated_at=models.DateTimeField(auto_now=True)
    #addresses: i can get the address using reveresd lookup

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
    
from django.db import models

class Book(models.Model):
    title=models.CharField(max_length=255)
    desc=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True) 
    updated_at=models.DateTimeField(auto_now=True)
    # authors
class Author(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    books=models.ManyToManyField(Book, related_name="authors")
    notes=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True) 
    updated_at=models.DateTimeField(auto_now=True)

def create_book(post):
    return Book.objects.create(title=post["title"], desc=post['description'])

def getbook(id):
    return Book.objects.get(id=id)

def create_author(post):
    return Author.objects.create(first_name=post['firstname'], last_name=post['lastname'], notes=post['notes'])

def getauthor(id):
    return Author.objects.get(id=id)

def allauthors():
    return Author.objects.all() 

def makeconenctions(id1,id2):
    auther = id1
    book = id2
    print(auther.id)
    print(book.id)
    auther.books.add(book)
# def addauthortobook(post):
#    auth= Author.objects.get(id = post['list'])
#    book = Book.objects.get(id = post[''])
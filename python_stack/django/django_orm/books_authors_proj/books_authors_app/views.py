from django.shortcuts import render, redirect
from . import models
from .models import create_book


def index(request): 
   context={
      'books': models.Book.objects.all(),
   }  

   return render(request, "index.html", context)

def author(request):
   context={
      'authors': models.Author.objects.all()
   }
   return render(request, 'addauthor.html', context)

def add_book(request):
   if request.method=="POST":
      book=models.create_book(request.POST)
      request.session['id']=book.id
      request.session['is_logged']=True
      
      return redirect('/')
   else:
      return redirect('/')
   
def book_detail(request, id):
   context={
      'book': models.getbook(id=id),
      'authors':models.allauthors()

   } 
   return render(request, 'bookdetail.html', context)

def add_author(request):
   if request.method=="POST":
      author=models.create_author(request.POST)
      request.session['id']=author.id
      request.session['is_logged']=True

      return redirect('author')
   else:
      return redirect('author')
   
def author_detail(request, id):
   context={
      'author': models.getauthor(id=id)
   }
   return render(request, 'authordetail.html', context)

def author_add(request,bookid):
   if request.method=="POST":
      id2= models.getbook(id=bookid)
      id1= models.getauthor(request.POST['list'])
      models.makeconenctions(id1,id2)
      return redirect(f'/bookdetail/{bookid}')
def book_add(request):
   if request.method=="POST":
      pass
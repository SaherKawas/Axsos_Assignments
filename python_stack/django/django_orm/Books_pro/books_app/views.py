from django.shortcuts import render, redirect
from . import models

def index(request):  

    context={
        "books": models.Book.objects.all(),
    } 
    return render(request, 'index.html', context)

def add_book(request):
    if request.method == "POST":
        book=models.create_book(request.POST)

    return redirect('/')

def book_detail(request, bookid):
    context={
        'book': models.getbook(id=bookid),
        'authors':models.allauthors()

    }
    return render(request, 'bookdetail.html', context)

def author(request):

    context={
        'authors': models.Author.objects.all()
    }
    return render (request, 'addauthor.html', context)

def add_author(request):
    if request.method=="POST":
        author=models.create_author(request.POST)
        return redirect('/author')
    
def author_detail(request, authorid):
    context={
        'author': models.getauthor(id=authorid)
    }

    return render(request, 'authordetail.html', context)
    
def author_list(request, bookid):
    if request.method == 'POST':
        id2= models.getbook(id=bookid)
        id1= models.getauthor(request.POST['list'])
        models.makeconenctions(id1,id2)

        return redirect(f'/bookdetail/{bookid}')
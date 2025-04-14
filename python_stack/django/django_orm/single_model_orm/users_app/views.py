from django.shortcuts import render, redirect
from . import models

def index(request):

    context={
        'first': models.User.objects.all()
    }
    return render(request, "index.html", context)

def form(request):
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        age=request.POST['age']

        myuser= models.create_user(request.POST) 

        request.session['id']=myuser.id

        return redirect ('/')
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
        request.session['is_logged']=True

        return redirect ('/')
    
def update_user(request):
    context={
        'user': models.get_user(request.session['id'])
    }
    return render(request, "update.html", context)
    
def update_post(request):
    if request.method=="POST" and "is_logged" in request.session:
        firstname=request.POST['new_firstname']
        lastname=request.POST['new_lastname']
        email=request.POST['new_email']
        age=request.POST['new_age']
        id=request.POST['user_id']

        updateduser= models.get_user(id) 
        updateduser.firstname=firstname
        updateduser.lastname=lastname
        updateduser.email=email
        updateduser.age=age

        updateduser.save()

        return redirect('/')
    

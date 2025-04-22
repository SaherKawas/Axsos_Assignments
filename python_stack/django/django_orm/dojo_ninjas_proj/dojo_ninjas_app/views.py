from django.shortcuts import render, redirect
from . import models


def index(request):

    context={
        'dojos': models.Dojo.objects.all(),
        'ninjas': models.Ninja.objects.all()
    }
    return render( request, "index.html", context)

def formdojo(request):
    if request.method=="POST":
        
        user= models.create_dojo(request.POST)
        request.session['id']=user.id
        request.session['is_logged']=True

        return redirect('/')
    else:
        return redirect('/')

def add_ninja(request):
    if request.method=="POST":

        models.create_ninja(request.POST)
        
        return redirect('/')
    
    return redirect('/')

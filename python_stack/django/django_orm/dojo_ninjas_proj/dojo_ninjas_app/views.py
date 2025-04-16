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
        name=request.POST['name']
        city=request.POST['city']
        state=request.POST['state']
        
        user= models.create_dojo(request.POST)
        request.session['id']=user.id
        request.session['is_logged']=True

        return redirect('/')
    else:
        return redirect('/')

def add_ninja(request):
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        dojo_id=request.POST['location']

        ninja= models.create_ninja(request.POST)
        
        return redirect('/')
    else:
        return redirect('/')

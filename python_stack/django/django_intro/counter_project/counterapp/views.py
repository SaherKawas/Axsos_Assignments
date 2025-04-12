from django.shortcuts import render, redirect

def index(request):

    if 'counter' not in request.session:
        request.session['counter']=0 #we assign a value of 0, to start from 0.

    else:
        request.session['counter']+=1

    context={
        "count":request.session['counter'],
        
    }
    return render (request, 'index.html', context)

def addtwovalue(request):
    request.session['counter'] +=1
    return redirect('/')

def clearsession(request):
    request.session.clear()
    return redirect('/')

def incrementbyuser(request):
    if request.POST and request.POST !='': # if request.POST: I should write it as a best practice, it is the same as if request.POST==0.
        input=int(request.POST['userinput']) # the post method gets data as a string, but here i need an iteger to add.
        request.session['counter']+=input-1
    return redirect('/')

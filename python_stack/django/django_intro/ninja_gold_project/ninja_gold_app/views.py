from django.shortcuts import render, redirect
import random 
from time import gmtime, strftime                  

def index(request):
    if 'gold' not in request.session:
        request.session['gold']=0
    if 'message' not in request.session:
        request.session['message'] = []
    
    context={
            'random': request.session['gold'],
            'message': request.session['message'],
            'time': strftime("%Y-%m-%d %H:%M %p", gmtime())
            
        }
    return render (request, "index.html", context)

def process(request):
    initiate=random.randint(10, 20)
    print(initiate)
    request.session['gold']+=initiate
    hidden=request.POST['building']
    message=f"You have entered a {hidden} and earned {initiate} gold"

    request.session['message'].append(message) 
    request.session.save()

    return redirect('/')

def quest(request):
    initiate=random.randint(-50, 50)
    print(initiate)
    request.session['gold']+=initiate

    if initiate<0:
        message=f"You failed a quest and lost {abs(initiate)} gold. Ouch"
    if initiate>0:
        message=f"You won a quest and won {initiate} gold. Bravo!"
    
    request.session['message'].append(message)  
    request.session.save()

    return redirect('/')
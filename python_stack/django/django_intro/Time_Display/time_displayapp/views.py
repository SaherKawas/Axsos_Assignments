from django.shortcuts import render, redirect
from time import gmtime, strftime

def show(request):
    return redirect("/time_display")

def index(request):
    
    context = {
        "date": strftime("%Y-%m-%d", gmtime()),
        "time": strftime("%H:%M %p", gmtime())
        
    }
    return render(request,'index.html', context)
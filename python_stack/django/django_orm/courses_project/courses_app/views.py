from django.shortcuts import render, redirect
from . import models
from django.contrib import messages
from .models import Course

def index(request): 

    context={
        'courses': models.Course.objects.all()
    }

    return render(request, 'index.html', context)

def add_course(request):
    if request.method == 'POST':
        errors=models.Course.objects.course_validator(request.POST)
        if len(errors)>0: 
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            models.create_course(request.POST)
            return redirect('/')
        

def display_course(request):
    context={
        'courses': models.Course.objects.all()
    }
    return render(request, 'index.html', context)

def delete_course_display(request, id):
    
    context={
        'course': models.getcourse(id=id)
    }
    return render (request, 'delete.html', context)

def delete_course(request, id):
    delete_course=models.deletecourse(id=id)
    return redirect('/')
    
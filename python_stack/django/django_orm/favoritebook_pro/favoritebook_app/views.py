from django.shortcuts import render, redirect
from . import models
import bcrypt
from .models import create_user
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def register_user(request):
    if request.method =='POST':
        errors=models.User.objects.basic_validator(request.POST)
        if len(errors)>0: 
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

        post= {
            'firstname': request.POST['firstname'],
            'lastname': request.POST['lastname'],
            'email': request.POST['email'],
            'password': pw_hash,  
        }
        new_user=models.create_user(post)

        return redirect('/')
    else:
        return redirect('/')
    
def login_user(request):
    if request.method == 'POST':
        
        email = request.POST['email']
        password = request.POST['password']

        if models.log_check(request.POST):
            request.session['is_logged'] = True
            context = {
                'user': models.getuser(email=email)
            }
            return render(request, 'books.html', context)
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('/') 
        
    else:
        
        messages.error(request, 'Bad request')
        return redirect('/')
    

def logout(request):
    request.session.flush()
    return redirect('/')
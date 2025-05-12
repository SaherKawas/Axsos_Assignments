from django.shortcuts import render, redirect
from . import models
from django.contrib import messages
import bcrypt


def index(request):
    return render(request, 'index.html')

def register_user(request):
    if request.method =='POST':
        errors=models.User.objects.register_validator(request.POST)
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
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']

        if models.log_check(request.POST):
            request.session['is_logged'] = True
            context = {
                'user': models.getuser(email=email)
            }
            return render(request, 'dashboard.html', context) 
        else:
            context = {
                'msg': 'Invalid email or password'
            }
            return render(request, 'index.html', context) 
    else:
        context = {
            'msg': 'Bad request'
        }
        return render(request, 'index.html', context)
    

def show_create(request):
    
    # context={
    #     'users': models.get_user(id=id)
    # }
    return render (request, 'createproject.html')

def display_project(request):
    if request.method =='POST':
        # errors=models.Project.objects.project_validator(request.POST)
        # if len(errors)>0: 
        #     for key, value in errors.items():
        #         messages.error(request, value)
        #     return redirect('/createproject')
        # else:
        new_project=models.create_project(request.POST)
        return render(f'/projectdetails/{new_project.id}')


def logout(request):
    request.session.flush()
    return redirect('/')


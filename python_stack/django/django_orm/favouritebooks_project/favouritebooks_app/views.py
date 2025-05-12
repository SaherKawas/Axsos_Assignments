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
        request.session['id']=new_user.id

        return redirect('/')
    else:
        return redirect('/')
    
def login_user(request):
    
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        if models.log_check(request.POST):
            request.session['is_logged'] = True
            user= models.getuser(email=email)
            request.session['id']=user.id
            books = models.allbooks()  
            context = {
                'user': user,
                'books': books  
            }
            return render(request, 'welcome.html', context) 
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
    
def add_book(request):

    if 'id' not in request.session:
        return redirect('/')
    
    if request.method =='POST':
        userid=request.session['id']
        new_book=models.create_book(request.POST, userid)
        user = models.User.objects.get(id=request.session['id'])
        books = models.allbooks()  

        context = {
        'user': user,
        'books': books
        }

        return render(request, 'welcome.html', context)    
    
def logout(request):
    request.session.flush()
    return redirect('/')


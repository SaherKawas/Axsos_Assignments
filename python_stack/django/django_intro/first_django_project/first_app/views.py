from django.shortcuts import render, HttpResponse, redirect
from . import models
from django.contrib import messages

def root(request):
    return HttpResponse("This is my first Django Project!")

def root(request):
    models.user.obrjects.create(first_name='test', last_name='test test')
    return render(request, "index.html")
 
def login(request):
    return render(request, "login.html")

def display_matches(request, leagueID, leagueCountry):

    if request.method== "GET":
        print(leagueID)#this shows on the terminal
        print(leagueCountry)#this shows on the terminal
        return render(request, "matches.html") #render to an HTML page
    else:
        return redirect("login") #redirects to a route
    
    # redirect deletes the DOM while render saves the DOM

def reg_form(request):
    return render (request, "registration.html")

def reg_form_post(request):
    if request.method=="POST":

        errors=models.User.objects.reg_validator(request.POST)
        if len(errors)>0: #if the length is a number >0 it means there is an error or more.
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/reg')
        else:
            name=request.POST['name']
            phonenumber=request.POST['phonenumber']
            address=request.POST['address']
        
            print(name)
            print(phonenumber)
            print(address) #we print to see if the data reached the backend from the frontend

            myuser= models.create_user(request.POST) 

            request.session['name']= name #this is the name filled in the registration form
            request.session['is_logged']=True
            request.session['id']=myuser.id
        return redirect("/home") # the methods in python should have a return
    else:
        return redirect("/matches/11/FR")
    
# the methods in python should have a return.
# successeful post request means that the data was stored in Database.
#if you define a session in any method, then it applies to every method because it is statefull.
#in django, the session is stored on browsers. so it behaves like a cookie but named a session.
#don't forget to do the migrate
# the homepage should not be accessible to anyone( it should be accessed when you log in for ex).

def home_page(request):
    if "is_logged" in request.session:
        context={
            'users': models.User.objects.all()
        }
        return render(request, "home.html")
    else:
        return redirect('/login')
    
def log_out(request):
    del request.session['name']
    del request.session['is_logged']
    del request.session['id']
    return redirect('/')

def update_user(request):
    context={
        'user': models.get_user(request.session['id'])
    }
    return render(request, "update.html", context)

# ORM post re
def update_post(request):

    if request.method=="POST" and "is_logged" in request.session:
            name=request.POST['new_name']
            phonenumber=request.POST['new_phonenumber']
            address=request.POST['new_address']
            id=request.POST['user_id']
        
            print(name) 
            print(phonenumber)
            print(address) #we print to see if the data reached the backend from the frontend

            updateduser= models.get_user(id) 
            updateduser.name=name
            updateduser.phonenumber=phonenumber
            updateduser.address=address

            updateduser.save()

            
            return redirect("/home") # the methods in python should have a return
    else:
        return redirect("/matches/11/FR")
    
def delete_form(request):

    if request.method=="POST":
        if "id" in request.session:
            models.delete_user_from_DB(request.session['id'])
            return  redirect('/home')
        else:
            return redirect('/')
    else:
        return redirect('/')
    
def delete_by_user_id(request):
    if request.method=="POST":
        models.delete_user_from_DB(request.POST['user_id'])
    

def addaddress(request):
    return render (request, "addaddress.html")

def address_add_form(request):
    city=request.post['ccity']
    country=request.POST['country']
    mohammadkhaseeb=

    models.Address.objects.create(city=city, country=country, )

def login_form(request):
    if request.method == 'POST':
        name=request.POST['name']
        password=request.POST['password']
        models.log_check(request.POST)
    else:
        context={
            'msg': 'Bad request'
        }
        return render(request, 'index.html')

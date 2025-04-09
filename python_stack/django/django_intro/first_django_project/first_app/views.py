from django.shortcuts import render, HttpResponse, redirect

def root(request):
    return HttpResponse("This is my first Django Project!")

def root(request):
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
        name=request.POST['name']
        phonenumber=request.POST['phonenumber']
        address=request.POST['address']
        id=request.POST['id']
        print(name)
        print(phonenumber)
        print(address) #we print to see if the data reached the backend from the frontend
        request.session['name']= name #this is the name filled in the registration form
        request.session['is_logged']=True
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
        return render(request, "home.html")
    else:
        return redirect('/login')
    
def log_out(request):
    del request.session['name']
    del request.session['is_logged']
    return redirect('/')


    



        
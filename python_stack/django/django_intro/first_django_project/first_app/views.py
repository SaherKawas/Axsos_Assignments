from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

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
        return redirect("login") #redirect to a route
    
    # redirect deletes the DOM while render save the DOM

def reg_form(request):
    return render (request, "registration.html")

def reg_form_post(request):
    if request.method=="post":
        
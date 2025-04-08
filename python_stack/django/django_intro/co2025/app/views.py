from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("response from index method from root route, localhost:8000!")

def batata(request):
    return render(request, "index.html")
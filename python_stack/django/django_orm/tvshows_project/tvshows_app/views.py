from django.shortcuts import render, redirect
from . import models

def index(request): 
    return redirect('/shows')

def show_tvlist(request):
    context={
            'shows': models.Show.objects.all()
        }
    return render (request, 'shows.html', context)

def add_new_show(request):
    return render (request, 'addshow.html')

def create_tvshow(request):
    if request.method == "POST":
        new_show=models.create_tv_show(request.POST)
        return redirect(f'/displaytvshow/{new_show.id}')
    
def display_tvshow(request, id):
    context={
        "show": models.getshow(id=id)
    }

    return render(request, 'tvshowdisplay.html', context)

def edit_tvshow(request, id):
    context={
        'show':models.Show.objects.get(id=id)
    }
    return render(request, 'editshow.html',context)

def tvshow_edit(request, id):
    if request.method=='POST':
        show=models.edit_tv_show(request.POST, id)
        return redirect(f'/displaytvshow/{id}')
    
    else:
        return redirect('/shows')

def delete_show(request, id):
    # if request.method == "POST":
    deleteshow= models.deleteshow(id=id)
    return redirect('/shows')
  
    

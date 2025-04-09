from django.urls import path
from . import views

urlpatterns = [    
    
    path('', views.index),
    path('addtwovalue', views.addtwovalue),
    path('destroysession', views.clearsession),
    path('incrementbyuser', views.incrementbyuser)
    
               
               ]
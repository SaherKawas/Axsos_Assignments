from django.urls import path
from . import views
urlpatterns = [    
    path('', views.index),
    path('register', views.register_user), 
    path('dashboard', views.login_user),
    path('createproject', views.show_create),
    path('loggedout', views.logout),
    path('projectdetails', views.display_project)
         
    ]

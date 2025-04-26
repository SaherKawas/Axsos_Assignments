from django.urls import path
from . import views
urlpatterns = [    
    path('', views.index),
    path('register', views.register_user),
    path('success', views.login_user),
    path('loggedout', views.logout)
    
    ]

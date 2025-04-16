from django.urls import path
from . import views
urlpatterns = [    
    
    path('', views.index),
    path('adddojo', views.formdojo),
    path('addninja', views.add_ninja)
    ]

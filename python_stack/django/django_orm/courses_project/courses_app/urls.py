from django.urls import path
from . import views
urlpatterns = [    
    path('', views.index),
    path('addcourse', views.add_course),
    path('displaycourse', views.display_course),
    path('deletecoursedisplay/<int:id>/', views.delete_course_display),
    path('deleteshow/<int:id>/', views.delete_course)
    ]

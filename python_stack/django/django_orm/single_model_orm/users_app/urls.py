from django.urls import path
from . import views
urlpatterns = [  
      path('', views.index), 
      path('form', views.form),
      path('update/', views.update_user),
      path('update_form', views.update_post)
      
         ]
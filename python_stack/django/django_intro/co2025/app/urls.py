from django.urls import path
from . import views    # the . indicates that the views file can be found in the same directory as this file
                    
urlpatterns = [
    path('', views.index), #what do you want me to display
    path("batata", views.batata)
]
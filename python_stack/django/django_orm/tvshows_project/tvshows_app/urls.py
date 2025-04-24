from django.urls import path
from . import views
urlpatterns = [    
    
    path('', views.index),
    path('shows/', views.show_tvlist),
    path('addnewshow/', views.add_new_show),
    path('createtvshow/', views.create_tvshow, name='create_tvshow'),
    path('displaytvshow/<int:id>', views.display_tvshow),
    path('edittvshow/<int:id>', views.edit_tvshow),
    path('tvshowedit/<int:id>', views.tvshow_edit),
    path('deleteshow/<int:id>/', views.delete_show)
    ]

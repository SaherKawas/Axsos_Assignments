from django.urls import path
from . import views
urlpatterns = [    
    
    path('', views.index),
    path('addbook', views.add_book),
    path('bookdetail/<int:id>', views.book_detail),
    path('authors', views.author),
    path('addauthor', views.add_author),
    path('authordetail/<int:id>', views.author_detail),
    path('authoradd/<int:bookid>', views.author_add),
    path('bookadd', views.book_add)

    
    ]

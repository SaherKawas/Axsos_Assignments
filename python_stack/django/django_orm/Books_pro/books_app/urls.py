from django.urls import path
from . import views
urlpatterns = [    
    
    path('', views.index),
    path('addbook', views.add_book),
    path('bookdetail/<int:bookid>', views.book_detail),
    path('author', views.author),
    path('addauthor', views.add_author),
    path('authordetail/<int:authorid>', views.author_detail),
    path('authorlist/<int:bookid>', views.author_list)
    
    ]



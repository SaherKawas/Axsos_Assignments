from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path("guess_num", views.guess),
    path("play_again", views.play),
    path("winners", views.win),
]
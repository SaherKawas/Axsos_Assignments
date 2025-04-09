from django.urls import path, include
from first_app import views

urlpatterns = [

    path("", views.root),
    path("login", views.login),
    path("matches/<int:leagueID>/<str:leagueCountry>", views.display_matches),
    path("reg", views.reg_form),
    path("reg_post", views.reg_form_post),
    path("home", views.home_page),
    path("log_out", views.logout)

]

# routes
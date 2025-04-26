from django.urls import path, include
from first_app import views

urlpatterns = [

    path("", views.root),
    path("login", views.login),
    path("matches/<int:leagueID>/<str:leagueCountry>", views.display_matches),
    path("reg", views.reg_form),
    path("reg_post", views.reg_form_post),
    path("home", views.home_page),
    path("log_out", views.logout),
    path("update", views.update_user),
    path('update_post', views.update_post),
    path('deleteform', views.delete_form),
    path("delete_user_by_user_id", views.delete_by_user_id),
    path('addaddress', views.addaddress),
    path('addressform', views.address_add_form),
    path('login_form', views.login_form)

]


from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('templates/', views.css, name="css"),
    path('templates/', views.django, name="django"),
    path('templates/', views.git, name="git"),
    path('templates/', views.html, name="html"),
    path('templates/', views.python, name="python"),
]

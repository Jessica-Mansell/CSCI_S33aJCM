from django.urls import path, include
from django.contrib import admin


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("css", views.css, name="css"),
    path("django", views.django, name="django"),
    path("git", views.git, name="git"),
    path("html", views.html, name="html"),
    path("python", views.python, name="python")
]

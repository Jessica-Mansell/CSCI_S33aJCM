from django.urls import path, include
from django.contrib import admin


from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('entries/<str:title>', views.info_page, name="title")
]

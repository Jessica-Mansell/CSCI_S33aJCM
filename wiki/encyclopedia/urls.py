from django.urls import path, include
from django.contrib import admin


from . import views

app_name ="wiki"

urlpatterns = [
    path('', views.index, name="index"),
    path('<str:title>', views.info_page, name="title")
]

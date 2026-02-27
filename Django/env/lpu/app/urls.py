from django.urls import path
from django.shortcuts import render
from app.views import *
urlpatterns = [
    path("",lpu,name="render"),
    path("aboutlpu",aboutlpu,name="aboutlpu"),
    path("save_data",saveDataView,name="save_data"),
    path("delete_note/<int:id>/",delete_note,name="delete_note"),
    path("edit_note/<int:id>/",edit_note,name="edit_note"),
]


from django.urls import path
from . import views

urlpatterns = [
    path("", views.startseite, name="startseite"),
]
from django.urls import path
from . import views

urlpatterns = [
    path("courses/", views.courses, name="courses"),
    path("routine/", views.routine, name="routine"),
]

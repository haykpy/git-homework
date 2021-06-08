from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("greeting/", views.greeting),
    path("date/", views.date),
    path("print/", views.print_dict),
]
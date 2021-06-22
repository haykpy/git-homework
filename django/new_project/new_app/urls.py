from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("greeting/", views.greeting),
    path("date/", views.date),
    path("print/", views.print_dict),
    path("hello-html/", views.hello_html),
    path("homepage/", views.homepage, name="hello"),
    path("json_file/", views.json_file),
    path("user_message/", views.user_message),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('new_task/', views.create_task, name="create"),
    path('update_task/<int:task_id>/',views.update_task, name="task_update"),
]
from django.urls import path, re_path
from . import views

app_name = "todo"

urlpatterns = [
    path("", views.todo_list, name="todo_list"),

    # CURD
    path("create/", views.create_todo, name="create_todo"),
    re_path(r"^(?P<pk>\d+)/$", views.retreive_todo, name="retreive_todo"),
    re_path(r"^(?P<pk>\d+)/update/$", views.update_todo, name="update_todo"),
    re_path(r"^(?P<pk>\d+)/delete/$", views.delete_todo, name="delete_todo"),
]



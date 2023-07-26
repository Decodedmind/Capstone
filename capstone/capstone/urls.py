from django.contrib import admin
from django.urls import path
from mcewens.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("Mcewens/", hello_world, name="hello_world"),
    path("", index, name="index"),
    path("test/", EXAMPLE_create_menu_item_view, name="test"),
    path("restaurant_admin/", restaurant_admin, name="restaurant_admin"),
    path("delete/<name>", deleteMenuItem, name="delete"),
    path("menu/", menu_view, name="menu"),
    path("home/", home_view, name="home"),
    path("lunch/", lunch_view, name="lunch"),
]

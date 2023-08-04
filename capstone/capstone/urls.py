from django.contrib import admin
from django.urls import path
from mcewens.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("Mcewens/", hello_world, name="hello_world"),
    path("", home_view, name="home"),
    path("restaurant_admin/", restaurant_admin, name="restaurant_admin"),
    path("restaurant_admin/delete/<id>", delete_menu_item, name="delete"),
    path("menu/", menu_view, name="menu"),
    path("home/", home_view, name="home"),
    path("lunch/", lunch_view, name="lunch"),
    path("dinner/", dinner_view, name="dinner"),
    path("brunch/", brunch_view, name="brunch"),
    path("wine/", wine_view, name="wine"),
    path("restaurant_admin/edit/<id>", edit_menu_item, name="edit"),
]

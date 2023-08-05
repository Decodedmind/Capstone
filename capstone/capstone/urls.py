from django.contrib import admin
from django.urls import path, include
from mcewens.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name="home"),
    path("asdfasfasdfasdfas/", restaurant_admin, name="restaurant_admin"),
    path("asdfasfasdfasdfas/delete/<id>", delete_menu_item, name="delete"),
    path("asdfasfasdfasdfas/edit/<id>", edit_menu_item, name="edit"),
    path("asdfasfasdfasdfas/confirm/", confirm_menu_item_view, name="confirm"),
    path("menu/", menu_view, name="menu"),
    path("home/", home_view, name="home"),
    path("lunch/", lunch_view, name="lunch"),
    path("dinner/", dinner_view, name="dinner"),
    path("brunch/", brunch_view, name="brunch"),
    path("wine/", wine_view, name="wine"),
    path("reservation/", reservation_view, name="reservation"),
    path("accounts/", include("django.contrib.auth.urls")),
    # path("accounts/profile/", profile_redirect, name="profile")
]

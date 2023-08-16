from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from mcewens.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name="home"),
    path("restaurant_admin/", restaurant_admin, name="restaurant_admin"),
    path("restaurant_admin/delete/<id>", delete_menu_item, name="delete"),
    path("restaurant_admin/edit/<id>", edit_menu_item, name="edit"),
    path("restaurant_admin/confirm/", confirm_menu_item_view, name="confirm"),
    path("menu/", menu_view, name="menu"),
    path("home/", home_view, name="home"),
    path("lunch/", lunch_view, name="lunch"),
    path("dinner/", dinner_view, name="dinner"),
    path("brunch/", brunch_view, name="brunch"),
    path("wine/", wine_view, name="wine"),
    path("reservation/", reservation_view, name="reservation"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("contact/", contact, name="contact"),
    path(
        "reset_password/", auth_views.PasswordResetView.as_view(), name="reset_password"
    ),
    path(
        "reset_password_sent/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset_password_complete/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

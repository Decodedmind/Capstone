from django.contrib import admin
from django.urls import path
from mcewens.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("Mcewens/", hello_world, name="hello_world"),
    path("", index, name="index"),
    path("test/", create_menu_item_view, name="test"),
]

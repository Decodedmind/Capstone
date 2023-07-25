from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import MenuItemForm
from . import models


def hello_world(request):
    return HttpResponse("Hello, World!")


def index(request):
    return render(request, "index.html")


# @login_required = uncomment this when admin page set up
def EXAMPLE_create_menu_item_view(request):
    if request.method == "POST":
        # Create object of form
        form = MenuItemForm(request.POST)
        # Generates an object from the form, but doesn't store it in the database
        item = form.save(commit=False)
        if form.is_valid():
            # if form is valid - which is should be always - spit all the information back on the screen
            # as an example
            context = {
                "id": item.id,
                "name": item.name,
                "price": item.price,
                "description": item.description,
                "category": item.category,
                "current": item.current,
                "form": form,
            }
        return render(request, "test.html", context)
    else:
        # if request method isn't post, the form hasn't been filled out yet.
        # Theoretically this won't trigger in the final product
        form = MenuItemForm()
        return render(request, "test.html", {"form": form})


def get_items_by_category_view(request):
    if request.method == "GET":
        category = request.GET.get("category")
        if category in ["Appetizer", "Lunch", "Dinner", "Dessert", "Wine"]:
            items = models.get_current_by_category(category)
            return HttpResponse(items)
    return HttpResponse("Invalid category")


def dinner_view(request):
    return render(request, "dinner.html")


def home_view(request):
    return render(request, "home.html")


"""
NEEDED ON FRONT END: BUTTON TO RETURN STRING OF "CATEGORY" TO THIS FUNCTION 
Categories are: Appetizer, Lunch, Dinner, Dessert, Wine
This is EXACTLY as written, so make sure you account for that before calling the function 
"""


# def EXAMPLE_current_items_by_category_view(request):
#     context = {"items": models.get_current_by_category("Wine")}

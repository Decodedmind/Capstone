from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import MenuItemForm
from . import models
from .models import *

# research block styles - could fix issue with image on menu page


def hello_world(request):
    return HttpResponse("I am beautiful")


def index(request):
    return render(request, "index.html")


def deleteMenuItem(request, id):
    menuItemId = id
    if request.method == "POST":
        if request.POST.get("yesno") == "YES":
            delete_menu_item(menuItemId)
            return redirect("restaurant_admin")
        else:
            return redirect("restaurant_admin")

    return render(request, "delete.html")


def editMenuItem(request, id):
    menuItemId = id
    menuItem = MenuItem.objects.get(id=menuItemId)
    form = MenuItemForm(instance=menuItem)

    if request.method == "POST":
        form = MenuItemForm(request.POST, instance=menuItem)
        if form.is_valid():
            form.save()
            return redirect("restaurant_admin")

    context = {"form": form}
    return render(request, "edit.html", context)


# def restaurant_admin(request):
#     form = MenuItemForm()
#     menuItems = MenuItem.objects.all()
#     if request.method == "POST":
#         form = MenuItemForm(request.POST)
#         name = request.POST.get("name")
#         description = request.POST.get("description")
#         price = request.POST.get("price")
#         create_menu_item(name, description, price)

#     context = {"form": form, "menuItems": menuItems}
#     return render(request, "restaurantadmin.html", context)


# @login_required
def restaurant_admin(request):
    menuItems = MenuItem.objects.all()
    if request.method == "POST":
        # Create object of form
        form = MenuItemForm(request.POST)
        # Generates an object from the form, but doesn't store it in the database
        # IF they create an error message, it resets the page without breaking everything
        try:
            item = form.save(commit=False)
            if form.is_valid():
                # if form is valid - which is should be always - spit all the information back on the screen
                # as an example
                form = MenuItemForm()
                context = {
                    "id": item.id,
                    "name": item.name,
                    "price": item.price,
                    "description": item.description,
                    "category": item.category,
                    "current": item.current,
                    "item_type": item.item_type,
                    "form": form,
                    "menuItems": menuItems,
                }
                item.save()
        except:
            # If the try fails, it's almost guaranteed to be an issue with the .save()s, which means duplicate data
            # Thus, this error message. Can rewrite it.
            error = "Something went wrong! Perhaps a menu item with this name and category already exists?"
            form = MenuItemForm()
            context = {"error": error, "menuItems": menuItems, "form": form}

        # It's possible to add an "Is this information correct?" prompt followed by another click,
        # Then you would just do item.save() if they click yes, else return to the form page
        return render(request, "restaurantadmin.html", context)
    else:
        # if request method isn't post, the form hasn't been filled out yet.
        # Theoretically this won't trigger in the final product
        form = MenuItemForm()
        return render(
            request, "restaurantadmin.html", {"form": form, "menuItems": menuItems}
        )


def get_items_by_category_view(request):
    if request.method == "GET":
        category = request.GET.get("category")
        if category in ["Appetizer", "Lunch", "Dinner", "Dessert", "Wine"]:
            items = models.get_current_by_category(category)
            return HttpResponse(items)
    return HttpResponse("Invalid category")


def dinner_view(request):
    TYPES = ("Appetizers", "Salads", "Entrees", "Desserts", "Wine", "Cocktails")
    # get sub categories, pass in separately
    dinner_item = get_current_by_category("Dinner").values()
    return render(request, "dinner.html", {"types": TYPES, "items": dinner_item})


def home_view(request):
    return render(request, "home.html")


def lunch_view(request):
    TYPES = ("Salads", "Sandwiches", "Entrees")
    # get sub categories, pass in separately
    lunch_item = get_current_by_category("Lunch").values()
    return render(request, "lunch.html", {"types": TYPES, "items": lunch_item})


def brunch_view(request):
    TYPES = ("Salads", "Sandwiches", "Entrees")
    # get sub categories, pass in separately
    brunch_item = get_current_by_category("Brunch").values()
    return render(request, "sundaybrunch.html", {"types": TYPES, "items": brunch_item})


def wine_view(request):
    TYPES = ("Wine", "Cocktails")
    # get sub categories, pass in separately
    wine_item = get_current_by_category("Wine and Cocktails").values()
    return render(request, "wine.html", {"types": TYPES, "items": wine_item})


def menu_view(request):
    return render(request, "menu.html")

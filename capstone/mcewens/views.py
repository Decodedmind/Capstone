from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import MenuItemForm, MenuUpdateForm
from . import models
from .models import *

# research block styles - could fix issue with image on menu page


def home_view(request):
    return render(request, "home.html")


def menu_view(request):
    return render(request, "menu.html")


def index(request):
    return render(request, "index.html")


def reservation_view(request):
    return render(request, "reservation.html")


def delete_menu_item(request, id):
    if request.method == "POST":
        if request.POST.get("yesno") == "YES":
            delete_menu_item_by_id(id)
            return redirect("restaurant_admin")
        else:
            return redirect("restaurant_admin")

    return render(request, "delete.html")


def edit_menu_item(request, id):
    menu_item = MenuItem.objects.get(id=id)
    form = MenuUpdateForm(instance=menu_item)

    if request.method == "POST":
        form = MenuUpdateForm(request.POST, instance=menu_item)
        if form.is_valid():
            form.save()
            return redirect("restaurant_admin")
        else:
            context[
                "error"
            ] = "Something went wrong! Perhaps a menu item with this name and category already exists?"

    context = {"form": form, "mode": "Edit"}
    return render(request, "edit.html", context)


def confirm_menu_item_view(request):
    item = request.session.get("item_input", None)
    # This pulls the cached data back out and sets it up in a dictionary for us
    new_item = {
        "name": item.get("name"),
        "description": item.get("description"),
        "category": item.get("category"),
        "item_type": item.get("item_type"),
        "price": item.get("price"),
    }
    # If the user edits the form on the page, it goes with that
    # Else it defers to what was already there
    form = MenuItemForm(request.POST or new_item)
    context = {"form": form, "mode": "Create"}
    if request.method == "POST":
        form = MenuItemForm(request.POST)
        try:
            form.save()
            return redirect("restaurant_admin")
        # If the try fails, it's because he edited something to be different, so we throw the error up.
        # Otherwise we just redirect.
        except:
            context[
                "error"
            ] = "Something went wrong! Perhaps a menu item with this name and category already exists?"

    return render(request, "edit.html", context)


# @login_required
def restaurant_admin(request):
    menu_items = MenuItem.objects.all()
    if request.method == "POST":
        form = MenuItemForm(request.POST)
        # If the form is valid, we clean the data up and store is as a cookie in the session
        # Then we redirect to a confirmation page where he can review it before saving.
        # This prevents refreshing from sending duplicate data, and also saves hassle if user messes up.
        if form.is_valid():
            request.session["item_input"] = form.cleaned_data
            return redirect("confirm")

        # If they create an error message, it resets the page without breaking everything
        else:
            # If validate fails, it's because of the unique flag blocking it.
            # Thus, this error message. Can rewrite it.
            error = "Something went wrong! Perhaps a menu item with this name and category already exists?"
            context = {"error": error, "menu_items": menu_items, "form": form}
        return render(request, "restaurant_admin.html", context)
    else:
        form = MenuItemForm()
        return render(
            request, "restaurant_admin.html", {"form": form, "menu_items": menu_items}
        )


def get_items_by_category_view(request):
    if request.method == "GET":
        category = request.GET.get("category")
        if category in ["Appetizer", "Lunch", "Dinner", "Dessert", "Wine"]:
            items = models.get_current_by_category(category)
            return HttpResponse(items)
    return HttpResponse("Invalid category")


def dinner_view(request):
    TYPES = ("Appetizers", "Salads", "Entrees")
    # get sub categories, pass in separately
    dinner_item = get_current_by_category("Dinner").values()
    return render(request, "dinner.html", {"types": TYPES, "items": dinner_item})


def lunch_view(request):
    TYPES = ("Salads", "Sandwiches", "Entrees")
    # get sub categories, pass in separately
    lunch_item = get_current_by_category("Lunch").values()
    return render(request, "lunch.html", {"types": TYPES, "items": lunch_item})


def brunch_view(request):
    TYPES = ("Salads", "Sandwiches", "Entrees")
    # get sub categories, pass in separately
    brunch_item = get_current_by_category("Brunch").values()
    return render(request, "sunday_brunch.html", {"types": TYPES, "items": brunch_item})


def wine_view(request):
    TYPES = ("Wine", "Cocktails")
    # get sub categories, pass in separately
    wine_item = get_current_by_category("Wine and Cocktails").values()
    return render(request, "wine.html", {"types": TYPES, "items": wine_item})


def profile_redirect(request):
    return redirect("restaurant_admin")

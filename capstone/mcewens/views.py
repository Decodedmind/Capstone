from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import MenuItemForm


def hello_world(request):
    return HttpResponse("Hello, World!")


def index(request):
    return render(request, "index.html")


# @login_required
def create_menu_item_view(request):
    if request.method == "POST":
        # Create object of form
        form = MenuItemForm(request.POST)
        item = form.save(commit=False)
        if form.is_valid():
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
        form = MenuItemForm()
        return render(request, "test.html", {"form": form})

from django.db import models


# one model - menu item
class MenuItem(models.Model):
    # Name - check
    name = models.CharField(max_length=50)

    # Category - Lunch/ Dinner / Brunch / Wine - check
    CATEGORY_CHOICES = (
        ("Brunch", "Brunch"),
        ("Lunch", "Lunch"),
        ("Dinner", "Dinner"),
        ("Wine and Cocktails", "Wine and Cocktails"),
    )

    category = models.CharField(choices=CATEGORY_CHOICES, max_length=50)

    TYPE_CHOICES = (
        ("Appetizers", "Appetizers"),
        ("Salads", "Salads"),
        ("Entrees", "Entrees"),
        ("Sandwiches", "Sandwiches"),
        ("Desserts", "Desserts"),
        ("Wine", "Wine"),
        ("Cocktails", "Cocktails"),
    )

    item_type = models.CharField(choices=TYPE_CHOICES, max_length=50, blank=True)
    # Types of item for the sake of menu

    # Description - check
    description = models.CharField(max_length=200, blank=True)

    # Price - check
    price = models.FloatField()

    # Current item? check
    current = models.IntegerField(default=1)

    class Meta:
        unique_together = ("name", "category")


# Constructor - default values left blank
def create_menu_item(name, description, price):
    item = MenuItem(
        name=name.title(),
        description=description,
        price=price,
    )
    item.save()
    return item


def get_current_items():
    return MenuItem.objects.filter(current=1)


def get_menu_items_by_category(cat):
    return MenuItem.objects.filter(category=cat)


def get_menu_items_by_name(name):
    try:
        return MenuItem.objects.get(name=name.title())
    except:
        return "No results found!"


def get_current_by_category(cat):
    return MenuItem.objects.filter(category=cat, current=1)


def set_current_status(item_id, status):
    try:
        item = MenuItem.objects.get(id=item_id)
        item.current = status
        item.save()
        return item
    except:
        raise ValueError("Item not found in database!")


# Should be able to change the category
def set_category(item_id, cat):
    try:
        item = MenuItem.objects.get(id=item_id)
        item.category = cat
        item.save()
        return item
    except:
        raise ValueError("Item not found in database!")


def set_menu_item_name(item_id, new_n):
    try:
        item = MenuItem.objects.get(id=item_id)
        item.name = new_n
        item.save()
        return item
    except:
        raise ValueError("Item not found in database!")


def set_menu_item_description(item_id, new_d):
    try:
        item = MenuItem.objects.get(id=item_id)
        item.description = new_d
        item.save()
        return item
    except:
        raise ValueError("Item not found in database!")


def set_menu_item_price(item_id, new_p):
    try:
        item = MenuItem.objects.get(id=item_id)
        item.price = new_p
        item.save()
        return item
    except:
        raise ValueError("Item not found in database!")


def delete_menu_item(name):
    try:
        item = get_menu_items_by_name(name)
        item.delete()
        return "Deleted!"
    except:
        raise ValueError("Item not found in database!")

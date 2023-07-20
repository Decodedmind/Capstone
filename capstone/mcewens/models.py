from django.db import models


# one model - menu item
class MenuItem(models.Model):
    # Name - check
    name = models.CharField(max_length=50)

    # Category - Lunch/ Dinner / Desert / Wine - check
    CATEGORY_CHOICES = (
        ("Unselected", "Unselected"),
        ("Lunch", "Lunch"),
        ("Dinner", "Dinner"),
        ("Dessert", "Dessert"),
        ("Wine", "Wine"),
    )

    category = models.CharField(
        choices=CATEGORY_CHOICES, default="Unselected", max_length=50, blank=True
    )
    # Possibility of making exclusive toggle for ease of use? If Lunch, not WIne? Research?

    # Description - check
    description = models.CharField(max_length=50, blank=True)

    # Price - check
    price = models.FloatField()
    # Price percentage option?

    # Current item? check
    current = models.IntegerField(default=1)


# Constructor - default values left blank
def create_menu_item(name, description, price):
    item = MenuItem(
        name=name,
        description=description,
        price=price,
    )
    item.save()
    return item


def get_current_items():
    return MenuItem.objects.filter(current=1)


def get_menu_items_by_category(cat):
    return MenuItem.objects.filter(category=cat)


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


def change_menu_item_name(item_id, new_n):
    try:
        item = MenuItem.objects.get(id=item_id)
        item.name = new_n
        item.save()
        return item
    except:
        raise ValueError("Item not found in database!")


def change_menu_item_description(item_id, new_d):
    try:
        item = MenuItem.objects.get(id=item_id)
        item.description = new_d
        item.save()
        return item
    except:
        raise ValueError("Item not found in database!")


def change_menu_item_price(item_id, new_p):
    try:
        item = MenuItem.objects.get(id=item_id)
        item.price = new_p
        item.save()
        return item
    except:
        raise ValueError("Item not found in database!")


# Submit button for forms?

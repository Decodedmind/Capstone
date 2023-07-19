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
    description = models.CharField(
        max_length=50, blank=True, null=True
    )  # should null be true?

    # Price - check
    price = models.FloatField()
    # Price percentage option?

    # Current item? check
    current = models.IntegerField(default=1)


def create_menu_item(name, category, description, price, current):
    item = MenuItem(
        name=name,
        category=category,
        description=description,
        price=price,
        current=current,
    )
    item.save()
    return item


# Submit button for forms

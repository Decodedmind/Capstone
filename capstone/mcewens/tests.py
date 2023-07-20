from django.test import TestCase
from . import models


class Test_MenuItem(TestCase):
    def setUp(self) -> None:
        self.item1 = models.create_menu_item(
            "Test1",
            "This is a dish",
            50.00,
        )
        self.item2 = models.create_menu_item(
            "Test2",
            "This is a dish",
            50.00,
        )
        self.item3 = models.create_menu_item(
            "Test3",
            "This is a dish",
            50.00,
        )

    def test_create_menu_item(self):
        assert self.item1.id == 1
        assert self.item1.name == "Test1"
        assert self.item1.description == "This is a dish"
        assert self.item1.price == 50.00
        assert self.item1.current == 1
        assert self.item1.category == "Unselected"

    def test_current_items(self):
        # Default to current
        assert len(models.get_current_items()) == 3

        # Can we change status?
        models.set_current_status(self.item2.id, 0)
        self.item2.refresh_from_db()
        assert self.item2.current == 0
        assert len(models.get_current_items()) == 2

        # Can we change status??
        models.set_current_status(self.item1.id, 0)
        models.set_current_status(self.item2.id, 1)
        self.item1.refresh_from_db()
        self.item2.refresh_from_db()
        assert self.item1.current == 0
        assert self.item2.current == 1
        assert len(models.get_current_items()) == 2

        # Can we change everything's status?
        models.set_current_status(self.item2.id, 0)
        models.set_current_status(self.item3.id, 0)
        self.item2.refresh_from_db()
        self.item3.refresh_from_db()
        assert self.item2.current == 0
        assert self.item3.current == 0
        assert len(models.get_current_items()) == 0

    def test_category_for_items(self):
        # Should default to unselected
        assert len(models.get_menu_items_by_category("Unselected")) == 3

        models.set_category(self.item1.id, "Wine")
        self.item1.refresh_from_db()
        assert self.item1.category == "Wine"
        assert len(models.get_menu_items_by_category("Unselected")) == 2
        assert len(models.get_menu_items_by_category("Wine")) == 1

    def test_change_name(self):
        assert self.item1.name == "Test1"
        models.change_menu_item_name(self.item1.id, "New")
        self.item1.refresh_from_db()
        assert self.item1.name == "New"

    def test_change_price(self):
        assert self.item2.price == 50
        models.change_menu_item_price(self.item2.id, 100)
        self.item2.refresh_from_db()
        assert self.item2.price == 100

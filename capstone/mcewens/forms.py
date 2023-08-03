from django import forms
from .models import MenuItem


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = [
            "name",
            "price",
            "description",
            "category",
            "item_type",
        ]
        exclude = ["current"]

# class deleteForm(forms.ModelForm):
#     itemId = forms.IntegerField(required=True)
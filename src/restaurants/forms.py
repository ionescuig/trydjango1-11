from .validators import validate_category
from .models import RestaurantLocation
from django import forms


class RestaurantCreateForm(forms.Form):
    name = forms.CharField()
    location = forms.CharField(required=False)
    category = forms.CharField(required=False)


class RestaurantLocationCreateForm(forms.ModelForm):
    # category = forms.CharField(required=False, validators=[validate_category])

    class Meta:
        model = RestaurantLocation
        fields = [
            'name',
            'location',
            'category',
        ]

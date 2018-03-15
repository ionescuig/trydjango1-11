from .validators import validate_category
from .models import RestaurantLocation
from django import forms


class RestaurantCreateForm(forms.Form):
    name = forms.CharField()
    location = forms.CharField(required=True)
    category = forms.CharField(required=False)


class RestaurantLocationCreateForm(forms.ModelForm):
    # category = forms.CharField(required=False, validators=[validate_category])
    name        = forms.CharField(label='Name',
                                  required=True,
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    location    = forms.CharField(label='Location',
                                  required=True,
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    category    = forms.CharField(label='Category',
                                  required=False,
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    slug        = forms.CharField(label='Slug (optional)',
                                  required=False,
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = RestaurantLocation
        fields = [
            'name',
            'location',
            'category',
            'slug',
        ]

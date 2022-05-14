from django import forms
from profiles.models import Profiles


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profiles
        fields = ["name", "age", "gender", "mobile",
                  "email", "city", "state", "country", "address", "image", ]

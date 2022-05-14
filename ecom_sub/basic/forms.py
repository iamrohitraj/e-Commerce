from basic.models import Consulting, Checkup
from django import forms


class CheckupForm(forms.ModelForm):
    class Meta():
        model = Consulting
        fields = "__all__"


class ConsultingForm(forms.ModelForm):
    class Meta():
        model = Checkup
        fields = "__all__"

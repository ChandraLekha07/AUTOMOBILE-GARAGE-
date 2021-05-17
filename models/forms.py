from django import forms

from .models import *

class DealsModelForm(forms.ModelForm):
    class Meta:
        model = Deals
        fields = '__all__'
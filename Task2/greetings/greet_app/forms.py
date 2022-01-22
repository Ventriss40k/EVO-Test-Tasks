from django import forms
from .models import *


class Your_name(forms.Form):
    name = forms.CharField(max_length=100)
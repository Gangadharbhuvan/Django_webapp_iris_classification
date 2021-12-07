from django import forms
from django.core import validators

class FormName(forms.Form):
    sepal_length = forms.FloatField(min_value=4.3, max_value=7.9, help_text="Enter the sepal length in floating point between 4.3 and 7.9")
    sepal_width = forms.FloatField(min_value=2.0, max_value=4.4, help_text="Enter the sepal width in floating point between 2.0 and 4.4")
    petal_length = forms.FloatField(min_value=1.0, max_value=6.9, help_text="Enter the petal length in floating point between 1.0 and 6.9")
    petal_width = forms.FloatField(min_value=0.1, max_value=2.5, help_text="Enter the petal width in floating point between 0.1 and 2.5")

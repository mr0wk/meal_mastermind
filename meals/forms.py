from django import forms

from .models import MealOccurrence


class MealOccurrenceForm(forms.ModelForm):
    class Meta:
        model = MealOccurrence
        fields = ["meals"]

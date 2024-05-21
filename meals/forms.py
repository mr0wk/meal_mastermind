from django import forms

from .models import Meal, MealOccurrence


class MealOccurrenceForm(forms.ModelForm):
    meals = forms.ModelMultipleChoiceField(
        queryset=Meal.objects.all(), widget=forms.CheckboxSelectMultiple, required=False
    )

    class Meta:
        model = MealOccurrence
        fields = ["meals"]

    def __init__(self, *args, **kwargs):
        if "instance" in kwargs:
            instance = kwargs["instance"]
            initial = kwargs.setdefault("initial", {})
            initial["meals"] = instance.meals.all()
        super().__init__(*args, **kwargs)

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, ListView, UpdateView

from meals.forms import MealOccurrenceForm
from meals.models import MealOccurrence


class PlannerView(ListView):
    model = MealOccurrence
    template_name = "planners/planner.html"
    context_object_name = "meal_occurrences"

    def get_queryset(self):
        date = self.kwargs["planner_date"]
        meal_occurrences = MealOccurrence.objects.filter(date=date).all()

        if not meal_occurrences:
            return None
        return meal_occurrences


def update_meal_occurrence_view(request, planner_date, meal_type):
    meal_occurrence, created = MealOccurrence.objects.get_or_create(
        date=planner_date, meal_type=meal_type
    )

    if request.method == "POST":
        form = MealOccurrenceForm(request.POST, instance=meal_occurrence)
        if form.is_valid():
            form.save()
            return redirect("planners:planner", planner_date=planner_date)
    else:
        form = MealOccurrenceForm(instance=meal_occurrence)

    return render(request, "planners/update_meal_occurrence.html", {"form": form})

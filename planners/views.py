from django.shortcuts import redirect, render
from django.views.generic import ListView

from meals.forms import MealOccurrenceForm
from meals.models import MealOccurrence


class PlannerView(ListView):
    model = MealOccurrence
    template_name = "planners/planner.html"
    context_object_name = "meal_occurrences"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        date = self.kwargs["planner_date"]
        meal_occurrences = MealOccurrence.objects.filter(date=date).all()

        context["meal_occurrences"] = meal_occurrences
        planner_date = self.kwargs["planner_date"]
        context["planner_date"] = planner_date
        return context


def update_meal_occurrence_view(request, planner_date, meal_type):
    # Get the MealOccurrence instance for the given date and meal type or create a new one
    meal_occurrence, created = MealOccurrence.objects.get_or_create(
        date=planner_date, meal_type=meal_type
    )

    if request.method == "POST":
        form = MealOccurrenceForm(request.POST, instance=meal_occurrence)
        if form.is_valid():
            # Save the form if there are any meals selected, otherwise delete the MealOccurrence instance
            if form.cleaned_data["meals"]:
                form.save()
            else:
                meal_occurrence.delete()
            return redirect("planners:planner", planner_date=planner_date)
    else:
        form = MealOccurrenceForm(instance=meal_occurrence)

    return render(request, "planners/update_meal_occurrence.html", {"form": form})

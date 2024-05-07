from django.views.generic import ListView

from meals.models import MealDate


class PlannerView(ListView):
    model = MealDate
    template_name = "core/planner.html"
    context_object_name = "meals"

    def get_queryset(self):
        date = self.kwargs["planner_date"]

        return MealDate.objects.filter(date=date).first().meals.all()

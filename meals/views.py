import datetime

from django.urls import reverse
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import Meal


class MealListView(ListView):
    context_object_name = "meals"

    def get_queryset(self):
        return Meal.objects.all()


class MealDetailView(DetailView):
    model = Meal


class MealUpdateView(UpdateView):
    model = Meal
    fields = ["name", "meal_type", "products"]

    def get_success_url(self):
        return reverse("meals:meal_detail", kwargs={"pk": self.object.pk})


class MealCreateView(CreateView):
    model = Meal
    fields = ["name", "meal_type", "products"]

    def get_success_url(self):
        return reverse("meals:meal_detail", kwargs={"pk": self.object.pk})


class MealDeleteView(DeleteView):
    model = Meal
    success_url = "/meals/"

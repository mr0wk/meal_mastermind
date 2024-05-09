from django.urls import path, register_converter

from . import views
from .converters import DateConverter

register_converter(DateConverter, "date")

app_name = "planners"
urlpatterns = [
    path("<date:planner_date>", views.PlannerView.as_view(), name="planner"),
    path(
        "<date:planner_date>/<str:meal_type>/add/",
        views.update_meal_occurrence_view,
        name="add_meal",
    ),
]

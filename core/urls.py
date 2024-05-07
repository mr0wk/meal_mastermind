from django.urls import path, register_converter

from . import views
from .converters import DateConverter

register_converter(DateConverter, "date")

app_name = "core"
urlpatterns = [
    path("planner/<date:planner_date>", views.PlannerView.as_view(), name="planner"),
]

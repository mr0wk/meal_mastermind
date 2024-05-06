from django.urls import path

from . import views

app_name = "meals"
urlpatterns = [
    path("", views.MealListView.as_view(), name="meal_list"),
    path("<int:pk>/", views.MealDetailView.as_view(), name="meal_detail"),
    path("new/", views.MealCreateView.as_view(), name="meal_new"),
    path("<int:pk>/edit/", views.MealUpdateView.as_view(), name="meal_edit"),
    path("<int:pk>/delete/", views.MealDeleteView.as_view(), name="meal_delete"),
]

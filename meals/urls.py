from django.urls import path
from . import views

app_name = 'meals'
urlpatterns = [
    path('', views.MealListView.as_view(), name='meal_list'),
    path('<int:pk>/', views.MealDetailView.as_view(), name='meal_detail'),
]
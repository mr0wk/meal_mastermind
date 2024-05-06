import datetime
from django.views.generic import ListView, DetailView, UpdateView
from .models import Meal


class MealListView(ListView):
    context_object_name = 'meals'

    def get_queryset(self):
        return Meal.objects.all()
    

class MealDetailView(DetailView):
    model = Meal


class MealUpdateView(UpdateView):
    model = Meal
    fields = ['name', 'meal_type', 'products']
    template_name_suffix = '_update_form'
    success_url = '/meals/'
    
    def form_valid(self, form):
        form.instance.updated_at = datetime.datetime.now()
        return super().form_valid(form)


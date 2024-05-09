from django.db import models


class Meal(models.Model):
    name = models.CharField(max_length=255)
    products = models.ManyToManyField("products.Product", related_name="meals")

    def __str__(self):
        return self.name


class MealOccurrence(models.Model):
    class MealType(models.TextChoices):
        BREAKFAST = "breakfast"
        LUNCH = "lunch"
        DINNER = "dinner"
        SNACK = "snack"

    meals = models.ManyToManyField(Meal)
    date = models.DateField()
    meal_type = models.CharField(
        max_length=10,
        choices=[(tag.value, tag.value) for tag in MealType],
        default=MealType.BREAKFAST.value,
    )

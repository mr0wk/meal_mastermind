# Generated by Django 5.0.4 on 2024-05-09 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0003_mealdate'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MealDate',
        ),
    ]
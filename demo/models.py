from django.db import models


class CookBook(models.Model):
    RECIPES = (
            (0, 'Hamburger'),
            (1, 'Pancake'))
    recipe_name = models.IntegerField(default=0,
            choices=RECIPES)
    ingridients = models.CharField(max_length=1024)


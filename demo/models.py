from django.db import models


class Ingridients(models.Model):
    # for hamburgers
    cheese  = models.IntegerField(default=0)
    ham     = models.IntegerField(default=0)
    onion   = models.IntegerField(default=0)
    bread   = models.IntegerField(default=0)
    ketchup = models.IntegerField(default=0)
    # for pancakes
    milk    = models.IntegerField(default=0)
    butter  = models.IntegerField(default=0)
    honey   = models.IntegerField(default=0)
    eggs    = models.IntegerField(default=0)
    # ...

class CookBook(models.Model):
    RECIPES = (
            (0, 'Hamburger'),
            (1, 'Pancake'))
    recipe_name = models.IntegerField(default=0,
            choices=RECIPES)
    ingridients = models.ForeignKey(Ingridients,
            on_delete=models.CASCADE)


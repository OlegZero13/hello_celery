from django.db import models


class Ingridients(models.Model):
    # for hamburgers
    cheese  = models.IntegerField(default=1)
    ham     = models.IntegerField(default=1)
    onion   = models.IntegerField(default=1)
    bread   = models.IntegerField(default=1)
    ketchup = models.IntegerField(default=1)
    # for pancakes
    milk    = models.IntegerField(default=100)
    butter  = models.IntegerField(default=200)
    honey   = models.IntegerField(default=0)
    eggs    = models.IntegerField(default=3)
    # ...

class CookBook(models.Model):
    recipe_name = models.CharField(max_length=48)
    ingridients = models.ForeignKey(Ingridients,
            on_delete=models.CASCADE)


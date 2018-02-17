from django.contrib import admin
from .models import Ingridients, CookBook

class Ingridients_AdminPanelDisplay(admin.ModelAdmin):
    exclude = []

class CookBook_AdminPanelDisplay(admin.ModelAdmin):
    exclude = []

admin.site.register(Ingridients, Ingridients_AdminPanelDisplay)
admin.site.register(CookBook, CookBook_AdminPanelDisplay)


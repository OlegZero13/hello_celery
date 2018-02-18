from django.contrib import admin
from .models import CookBook

class CookBook_AdminPanelDisplay(admin.ModelAdmin):
    exclude = []

admin.site.register(CookBook, CookBook_AdminPanelDisplay)


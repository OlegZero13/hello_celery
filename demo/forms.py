from django import forms
from .models import CookBook

#class HamburgerForm(forms.ModelForm):
#    class Meta:
#        model = Ingridients
#        fields = ['cheese', 'ham', 'onion', 'bread', 'ketchup']

#class PancakeForm(forms.ModelForm):
#    class Meta:
#        model = Ingridients
#        fields = ['milk', 'butter', 'honey', 'eggs']

class CookBookForm(forms.ModelForm):
    class Meta:
        model = CookBook
        exclude = ['ingridients']


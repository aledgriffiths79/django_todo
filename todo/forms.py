from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
  # inner class below to tell django what we want in the form
  class Meta:
    model= Item
    fields = ('name', 'done')


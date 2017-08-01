from django import forms

from . import models

class ThoughtForm(forms.ModelForm):
    class Meta:
        fields = {'notes', 'condition'}
        model = models.Thought
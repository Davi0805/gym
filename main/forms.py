from django import forms
from django.forms import ModelForm
from .models import Exercparametros


class ExercparametrosForm(forms.ModelForm):
    class Meta:
        model = Exercparametros
        fields = ('pesomax',)
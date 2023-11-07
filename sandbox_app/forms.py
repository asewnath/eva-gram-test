from django import forms
from .models import Plot

class PlotForm(forms.Form):
    plot = forms.ModelChoiceField(queryset=Plot.objects.values_list('title', flat=True).distinct(), 
                                   initial=0,
                                   to_field_name='title')
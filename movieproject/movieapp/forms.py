from django import forms

from movieapp.models import Movies


class MovieForm(forms.ModelForm):
    class Meta:
        model=Movies
        fields=['name','desc','year','img']


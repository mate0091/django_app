from django import forms
from .models import *

class ActorForm(forms.ModelForm):

    class Meta:
        model = Actor
        fields = "__all__"

class FilmActorForm(forms.ModelForm):

    class Meta:
        model = FilmActor
        fields = "__all__"

class FilmForm(forms.ModelForm):

    class Meta:
        model = Film
        fields = "__all__"

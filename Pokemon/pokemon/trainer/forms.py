from django.forms import ModelForm
from .models import Profile
from django import forms

class TrainerForm(ModelForm):

    class Meta:
        model = Profile
        fields = ['trainername']

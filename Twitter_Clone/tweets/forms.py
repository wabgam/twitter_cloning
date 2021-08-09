from django import forms
from .models import Tweet


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = '__all__'


class EditForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['name', 'body', 'image']

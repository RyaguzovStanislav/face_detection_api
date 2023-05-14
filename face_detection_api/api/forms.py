from django import forms
from .models import Picture
from django.utils.translation import gettext_lazy as _

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['title', 'photo']
        labels = {
            "title": "ghdfgdhfghgdhf",
            "photo": ""
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-title', 'font-size': '40px', 'color': '#eee'}),
            # 'photo': forms.ImageField(attrs={'class': 'form-photo', 'font-size': '40px', 'color': '#eee'})
        }
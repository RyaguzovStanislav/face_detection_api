from django import forms
from .models import Picture

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['title', 'photo']
        labels = {
            "title": "",
            "photo": ""
        }
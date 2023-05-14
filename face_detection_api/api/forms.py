from django import forms
from .models import Picture
from django.utils.translation import gettext_lazy as _

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['title', 'photo']
        labels = {
            "title": "",
            "photo": ""
        }
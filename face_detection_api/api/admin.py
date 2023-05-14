from django.contrib import admin
from .models import Picture

class ImageAdmin(admin.ModelAdmin):
    list_display = ["title", "photo"]

admin.site.register(Picture, ImageAdmin)

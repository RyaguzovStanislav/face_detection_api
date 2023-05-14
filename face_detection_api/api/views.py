import os

import cv2
from detection.main.run import MainRunner
from django.shortcuts import render, redirect
from .models import Picture
from .forms import ImageUploadForm
from django.conf import settings


def home_page(request):
    data = Picture.objects.all()
    context = {
        'data': data
    }
    return render(request, 'upload.html', context)


def upload_image(request):
    Picture.objects.all().delete()
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('detection')
    else:
        form = ImageUploadForm(initial={'title': 'Оригинальное фото'})
    return render(request, 'upload.html', {'form': form})


def detect_faces(path):
    detect_image = MainRunner(path).run()

    detect_image_path = os.path.join(settings.PATH_OUT, 'detect_img.jpg')
    cv2.imwrite(detect_image_path, cv2.cvtColor(detect_image, cv2.COLOR_RGB2BGR))

    Picture.objects.create(title='Распознанное фото', photo='out/detect_img.jpg')

    return detect_image_path



def detect_image(request):
    detect_faces(settings.PATH_IN)
    data = Picture.objects.all()
    context = {
        'data': data
    }
    return render(request, 'home_page.html', context)


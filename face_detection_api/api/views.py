import os

import cv2
from detection.main.run import MainRunner
from django.shortcuts import render, redirect
from .models import Picture
from .forms import ImageUploadForm
from django.conf import settings

# функция для загрузки пользователем изображения
def upload_image(request):
    data = Picture.objects.all()
    # чистка локального хранилища и базы данных при повторных запросах
    if data:
        os.remove(settings.PATH_FOR_CLEAN_FILE + data[0].photo.url)
        data.delete()

    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('detection')
    else:
        form = ImageUploadForm(initial={'title': 'Оригинальное фото'})
    return render(request, 'upload.html', {'form': form})

# функция содержащая функционал по распознанию лиц
def detect_faces(path):
    # распознавание лиц на фото с помощью библиотеки detection, возвращает размеченное изображение
    detect_image = MainRunner(path).run()

    # сохранение полученного изображения в локальное хранилище
    detect_image_path = os.path.join(settings.PATH_OUT, 'detect_img.jpg')
    cv2.imwrite(detect_image_path, cv2.cvtColor(detect_image, cv2.COLOR_RGB2BGR))

    # сохранение полученного изображения в базе данных
    Picture.objects.create(title='Распознанное фото', photo='out/detect_img.jpg')


# функция отвечающая за вывод данных на представление
def detect_image(request):
    detect_faces(settings.PATH_IN)
    data = Picture.objects.all()
    context = {
        'data': data
    }
    return render(request, 'home_page.html', context)


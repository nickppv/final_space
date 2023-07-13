from django.shortcuts import render
from .models import Galery
from random import choice


def index(request):
    # выбираем все записи из БД
    all_pictures = Galery.objects.all()
    # выбираем случайное изображения в превью слайдера
    preview_picture = choice(all_pictures)
    modal_answer = choice(['Пожалуй, хватит...',
                           'Я достаточно увидел',
                           'Я мухожук!',
                           'На выход -->',
                           'Выйти'])
    context = {
        'all_pictures': all_pictures,
        'preview_picture': preview_picture,
        'modal_answer': modal_answer,
        }
    return render(request, 'space_agency/index.html', context)

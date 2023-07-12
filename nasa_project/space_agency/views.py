from django.shortcuts import render
from .models import Galery


def index(request):
    all_pictures = Galery.objects.all()
    last_picture = all_pictures.last()
    context = {
        'all_pictures': all_pictures,
        'last_picture': last_picture
        }
    return render(request, 'space_agency/index.html', context)

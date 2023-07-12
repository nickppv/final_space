from django.shortcuts import render
from .models import Galery


def index(request):
    all_pictures = Galery.objects.all()
    context = {'all_pictures': all_pictures}
    return render(request, 'space_agency/index.html', context)

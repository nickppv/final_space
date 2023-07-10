from django.shortcuts import render


def index(request):
    return render(request, 'space_agency/index.html')

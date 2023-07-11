from django.urls import path

from space_agency import views

app_name = 'space_agency'

urlpatterns = [
    path('', views.index, name='index'),
]

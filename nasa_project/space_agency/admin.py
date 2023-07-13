from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

from .models import Galery


@admin.register(Galery)
class GaleryAdmin(SortableAdminMixin, admin.ModelAdmin):
    ordering = ['image']
    list_display = [
        'name',
        'description',
        'image'
        ]

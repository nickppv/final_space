from django.db import models
from filer.fields.image import FilerImageField


class Galery(models.Model):
    name = models.CharField(
        max_length=50,
        blank=True,
        default='Без названия',
        verbose_name='Название изображения',
        )
    image = FilerImageField(
        db_index=True,
        null=True,
        blank=True,
        related_name='image_galery',
        on_delete=models.SET_NULL,
        )
    description = models.TextField(
        blank=True,
        verbose_name='Описание'
        )

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

        ordering = ['image']

    def __str__(self):
        return self.name

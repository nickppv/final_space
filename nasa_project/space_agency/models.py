from django.db import models


class Galery(models.Model):
    name = models.CharField(
        max_length=50,
        blank=True,
        default='Название не было добавлено',
        verbose_name='Название изображения',
        )
    image = models.ImageField(upload_to='images')
    description = models.TextField(
        blank=True,
        verbose_name='Описание'
        )

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def __str__(self):
        return self.name

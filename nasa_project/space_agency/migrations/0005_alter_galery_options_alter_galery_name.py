# Generated by Django 4.1.10 on 2023-07-13 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space_agency', '0004_alter_galery_options_alter_galery_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='galery',
            options={'ordering': ['image'], 'verbose_name': 'Изображение', 'verbose_name_plural': 'Изображения'},
        ),
        migrations.AlterField(
            model_name='galery',
            name='name',
            field=models.CharField(blank=True, default='Без названия', max_length=50, verbose_name='Название изображения'),
        ),
    ]
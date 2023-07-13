# Generated by Django 4.1.10 on 2023-07-13 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space_agency', '0003_alter_galery_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='galery',
            options={'ordering': ['name'], 'verbose_name': 'Изображение', 'verbose_name_plural': 'Изображения'},
        ),
        migrations.AlterField(
            model_name='galery',
            name='name',
            field=models.CharField(blank=True, db_index=True, default='Без названия', max_length=50, verbose_name='Название изображения'),
        ),
    ]

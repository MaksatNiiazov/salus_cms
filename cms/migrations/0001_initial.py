# Generated by Django 5.1 on 2024-08-22 04:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('title_ru', models.CharField(max_length=200, null=True, verbose_name='Заголовок')),
                ('title_ky', models.CharField(max_length=200, null=True, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('description_ru', models.TextField(null=True, verbose_name='Описание')),
                ('description_ky', models.TextField(null=True, verbose_name='Описание')),
                ('image', models.ImageField(null=True, upload_to='about_us/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'О нас',
                'verbose_name_plural': 'О нас',
            },
        ),
        migrations.CreateModel(
            name='Advantages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название преимущества')),
                ('title_ru', models.CharField(max_length=200, null=True, verbose_name='Название преимущества')),
                ('title_ky', models.CharField(max_length=200, null=True, verbose_name='Название преимущества')),
                ('image', models.ImageField(blank=True, null=True, upload_to='advantages/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Преимущество',
                'verbose_name_plural': 'Преимущества',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('small_text', models.TextField(verbose_name='Короткий текст')),
                ('small_text_ru', models.TextField(null=True, verbose_name='Короткий текст')),
                ('small_text_ky', models.TextField(null=True, verbose_name='Короткий текст')),
                ('text', models.TextField(verbose_name='Текст')),
                ('text_ru', models.TextField(null=True, verbose_name='Текст')),
                ('text_ky', models.TextField(null=True, verbose_name='Текст')),
                ('phone_text', models.TextField(verbose_name='Текст для телефонов')),
                ('phone_text_ru', models.TextField(null=True, verbose_name='Текст для телефонов')),
                ('phone_text_ky', models.TextField(null=True, verbose_name='Текст для телефонов')),
                ('map', models.TextField(blank=True, null=True, verbose_name='Карта')),
                ('map_link', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ссылка на карту')),
            ],
            options={
                'verbose_name': 'Контактная информация',
                'verbose_name_plural': 'Контактная информация',
            },
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название застройщика')),
                ('name_ru', models.CharField(max_length=200, null=True, verbose_name='Название застройщика')),
                ('name_ky', models.CharField(max_length=200, null=True, verbose_name='Название застройщика')),
                ('description', models.TextField(verbose_name='Описание')),
                ('description_ru', models.TextField(null=True, verbose_name='Описание')),
                ('description_ky', models.TextField(null=True, verbose_name='Описание')),
                ('logo', models.ImageField(null=True, upload_to='developers/', verbose_name='Логотип')),
            ],
            options={
                'verbose_name': 'Застройщик',
                'verbose_name_plural': 'Застройщики',
            },
        ),
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('name_ru', models.CharField(max_length=100, null=True, verbose_name='Имя')),
                ('name_ky', models.CharField(max_length=100, null=True, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Телефон')),
                ('message', models.TextField(verbose_name='Сообщение')),
                ('message_ru', models.TextField(null=True, verbose_name='Сообщение')),
                ('message_ky', models.TextField(null=True, verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Запрос',
                'verbose_name_plural': 'Запросы',
            },
        ),
        migrations.CreateModel(
            name='MainBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('title_ru', models.CharField(max_length=200, null=True, verbose_name='Заголовок')),
                ('title_ky', models.CharField(max_length=200, null=True, verbose_name='Заголовок')),
                ('subtitle', models.CharField(max_length=200, verbose_name='Подзаголовок')),
                ('subtitle_ru', models.CharField(max_length=200, null=True, verbose_name='Подзаголовок')),
                ('subtitle_ky', models.CharField(max_length=200, null=True, verbose_name='Подзаголовок')),
                ('first_text_title', models.CharField(max_length=200, verbose_name='Заголовок первого текста')),
                ('first_text_title_ru', models.CharField(max_length=200, null=True, verbose_name='Заголовок первого текста')),
                ('first_text_title_ky', models.CharField(max_length=200, null=True, verbose_name='Заголовок первого текста')),
                ('first_text', models.TextField(verbose_name='Первый текст')),
                ('first_text_ru', models.TextField(null=True, verbose_name='Первый текст')),
                ('first_text_ky', models.TextField(null=True, verbose_name='Первый текст')),
                ('second_text_title', models.CharField(max_length=200, verbose_name='Заголовок второго текста')),
                ('second_text_title_ru', models.CharField(max_length=200, null=True, verbose_name='Заголовок второго текста')),
                ('second_text_title_ky', models.CharField(max_length=200, null=True, verbose_name='Заголовок второго текста')),
                ('second_text', models.TextField(verbose_name='Второй текст')),
                ('second_text_ru', models.TextField(null=True, verbose_name='Второй текст')),
                ('second_text_ky', models.TextField(null=True, verbose_name='Второй текст')),
            ],
            options={
                'verbose_name': 'Блок главной страницы',
                'verbose_name_plural': 'Блоки главной страницы',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название услуги')),
                ('title_ru', models.CharField(max_length=200, null=True, verbose_name='Название услуги')),
                ('title_ky', models.CharField(max_length=200, null=True, verbose_name='Название услуги')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AdvantageItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название преимущества')),
                ('title_ru', models.CharField(max_length=200, null=True, verbose_name='Название преимущества')),
                ('title_ky', models.CharField(max_length=200, null=True, verbose_name='Название преимущества')),
                ('description', models.TextField(verbose_name='Описание')),
                ('description_ru', models.TextField(null=True, verbose_name='Описание')),
                ('description_ky', models.TextField(null=True, verbose_name='Описание')),
                ('advantages', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='advantages', to='cms.advantages', verbose_name='Преимущество')),
            ],
            options={
                'verbose_name': 'Преимущество',
                'verbose_name_plural': 'Преимущества',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200, verbose_name='Адрес')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='cms.contact', verbose_name='Контакт')),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адреса',
            },
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название здания')),
                ('name_ru', models.CharField(max_length=200, null=True, verbose_name='Название здания')),
                ('name_ky', models.CharField(max_length=200, null=True, verbose_name='Название здания')),
                ('description', models.TextField(verbose_name='Описание')),
                ('description_ru', models.TextField(null=True, verbose_name='Описание')),
                ('description_ky', models.TextField(null=True, verbose_name='Описание')),
                ('image', models.ImageField(null=True, upload_to='buildings/', verbose_name='Изображение')),
                ('file', models.FileField(null=True, upload_to='buildings/', verbose_name='Файл')),
                ('developer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buildings', to='cms.developer')),
            ],
            options={
                'verbose_name': 'Здание',
                'verbose_name_plural': 'Здания',
            },
        ),
        migrations.CreateModel(
            name='Phones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phones', to='cms.contact', verbose_name='Контакт')),
            ],
            options={
                'verbose_name': 'Телефон',
                'verbose_name_plural': 'Телефоны',
            },
        ),
        migrations.CreateModel(
            name='ServiceItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название услуги')),
                ('title_ru', models.CharField(max_length=200, null=True, verbose_name='Название услуги')),
                ('title_ky', models.CharField(max_length=200, null=True, verbose_name='Название услуги')),
                ('description', models.TextField(verbose_name='Описание')),
                ('description_ru', models.TextField(null=True, verbose_name='Описание')),
                ('description_ky', models.TextField(null=True, verbose_name='Описание')),
                ('image', models.FileField(null=True, upload_to='services/', verbose_name='Изображение')),
                ('services', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='cms.services', verbose_name='Услуга')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.FileField(null=True, upload_to='social/', verbose_name='Иконка')),
                ('link', models.CharField(max_length=200, verbose_name='Ссылка')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social', to='cms.contact', verbose_name='Контакт')),
            ],
            options={
                'verbose_name': 'Социальная сеть',
                'verbose_name_plural': 'Социальные сети',
            },
        ),
        migrations.CreateModel(
            name='WorkTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200, verbose_name='День')),
                ('time', models.CharField(max_length=200, verbose_name='Время')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_time', to='cms.contact', verbose_name='Контакт')),
            ],
            options={
                'verbose_name': 'Время работы',
                'verbose_name_plural': 'Время работы',
            },
        ),
    ]

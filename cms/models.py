from django.core.exceptions import ValidationError
from django.db import models


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.pk and self.__class__.objects.exists():
            raise ValidationError(f"Нельзя создать больше одной записи {self.__class__.__name__}.")
        return super().save(*args, **kwargs)


class MainBlock(SingletonModel):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    subtitle = models.CharField(max_length=200, verbose_name='Подзаголовок')
    first_text_title = models.CharField(max_length=200, verbose_name='Заголовок первого текста')
    first_text = models.TextField(verbose_name='Первый текст')
    second_text_title = models.CharField(max_length=200, verbose_name='Заголовок второго текста')
    second_text = models.TextField(verbose_name='Второй текст')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блок главной страницы'
        verbose_name_plural = 'Блоки главной страницы'


class AboutUs(SingletonModel):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='about_us/', verbose_name='Изображение', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'


class Services(SingletonModel):
    title = models.CharField(max_length=200, verbose_name='Название услуги')

    def __str__(self):
        return self.title


class ServiceItem(models.Model):
    services = models.ForeignKey(Services, on_delete=models.CASCADE, related_name='services', verbose_name='Услуга')
    title = models.CharField(max_length=200, verbose_name='Название услуги')
    description = models.TextField(verbose_name='Описание')
    image = models.FileField(upload_to='services/', verbose_name='Изображение', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Advantages(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название преимущества')
    image = models.ImageField(upload_to='advantages/', blank=True, null=True, verbose_name='Изображение')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'


class AdvantageItem(models.Model):
    advantages = models.ForeignKey(Advantages, on_delete=models.CASCADE, related_name='advantages',
                                   verbose_name='Преимущество')
    title = models.CharField(max_length=200, verbose_name='Название преимущества')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'


class Developer(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название застройщика')
    description = models.TextField(verbose_name='Описание')
    logo = models.ImageField(upload_to='developers/', verbose_name='Логотип', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Застройщик'
        verbose_name_plural = 'Застройщики'


class Building(models.Model):
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE, related_name='buildings', null=True)
    name = models.CharField(max_length=200, verbose_name='Название здания')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='buildings/', verbose_name='Изображение', null=True)
    file = models.FileField(upload_to='buildings/', verbose_name='Файл', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Здание'
        verbose_name_plural = 'Здания'


class Inquiry(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(verbose_name='Электронная почта')
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name='Телефон')
    message = models.TextField(verbose_name='Сообщение')

    def __str__(self):
        return f"Запрос от {self.name}"

    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'


class Contact(models.Model):
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Электронная почта')
    address = models.TextField(verbose_name='Адрес')
    map = models.TextField(blank=True, null=True, verbose_name='Карта')

    def __str__(self):
        return f"Контакт {self.id}"

    class Meta:
        verbose_name = 'Контактная информация'
        verbose_name_plural = 'Контактная информация'
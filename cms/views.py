from django.contrib import messages
from django.contrib.messages import get_messages
from django.shortcuts import render, redirect
from django.views.generic import View
from .models import *


# Create your views here.


class SiteView(View):
    def get(self, request, *args, **kwargs):
        mainblock = MainBlock.objects.first()
        if not mainblock:
            mainblock = MainBlock.objects.create(
                title='SALUS.kg',
                subtitle='Система управления отелями и апартаментами',
                first_text_title='Большая база данных',
                first_text='Большая база данных о строящихся и продаваемых объектах недвижимых имуществ в нашем офисе',
                second_text_title='Большая база данных',
                second_text='Большая база данных о строящихся и продаваемых объектах недвижимых имуществ в нашем офисе',
            )
        aboutus = AboutUs.objects.first()
        if not aboutus:
            aboutus = AboutUs.objects.create(
                title='О нас',
                description='Наша компания предоставляет современную и удобную систему управления апартаментами для жильцов и собственников недвижимости. Мы стремимся обеспечить максимальный комфорт и безопасность нашим клиентам, предоставляя им возможность управлять своими апартаментами из любой точки мира. Наша система позволяет легко контролировать температуру, освещение, безопасность и другие параметры в апартаментах через мобильное приложение или веб-портал. Мы также предлагаем возможность заказа дополнительных услуг, таких как уборка, обслуживание и транспортные услуги, прямо через нашу платформу.',
            )
        service_title = Services.objects.first()
        if not service_title:
            service_title = Services.objects.create(
                title='Наши услуги',
            )
            services = ServiceItem.objects.create(
                services=service_title,
                title='Ремонт под ключ',
                description='Мы берем на себя все этапы работ: от разработки дизайн-проекта и закупки материалов до выполнения строительных и отделочных работ.',

            )
        services = ServiceItem.objects.all()
        advantages_title = Advantages.objects.first()
        if not advantages_title:
            advantages_title = Advantages.objects.create(
                title='Наши преимущества',
            )
        advantages = AdvantageItem.objects.all()
        if not advantages:
            advantages = AdvantageItem.objects.create(
                advantages=advantages_title,
                title='Большая база данных',
                description='Большая база данных о строящихся и продаваемых объектах недвижимых имуществ в нашем офисе',
            )
        developers = Developer.objects.all()
        if not developers:
            developers = Developer.objects.create(
                name='Застройщик',
                description='Описание',
            )

        buildings = Building.objects.all()
        if not buildings:
            buildings = Building.objects.create(
                name='ЖК Osh Plaza',
                description='ЖК Osh Plaza в Оше будет построен на участке площадь 1,12 га. Здание высотой в 14 этажей имеет классический архитектурный облик, а в отделке его фасадов используются только качественные натуральные материалы.',
            )
        conrtacts = Contact.objects.first()
        if not conrtacts:
            conrtacts = Contact.objects.create(
                text='Для получения консультации оставьте заявку, и мы свяжемся с вами.',
                small_text='Чтобы получить консультацию, свяжитесь с нами',
                phone_text='Так же вы можете связаться с нами по телефону',
            )

        message_exist = request.session.pop('message_exist', False)
        site_meta = SiteSettings.objects.first()
        if not site_meta:
            site_meta = SiteSettings.objects.create(
                site_name = 'SALUS',
                site_description = 'Salus.kg',
                meta_title = 'salus.kg',
                meta_description = 'salus.kg')

        context = {
            'main_block': mainblock,
            'about_us': aboutus,
            'service_title': service_title,
            'services': services,
            'advantages_title': advantages_title,
            'advantages': advantages,
            'developers': developers,
            'buildings': buildings,
            'contacts': conrtacts,
            'message_exist': message_exist,
            'site_meta': site_meta,
        }

        return render(request, 'index.html', context=context)


class CreateRequestView(View):
    def get(self, request):
        message_exist = request.session.pop('message_exist', False)
        return render(request, 'index.html', {'message_exist': message_exist})

    def post(self, request):
        name = request.POST.get('name', 'Неизвестно')
        phone = request.POST.get('phone', 'Неизвестно')
        email = request.POST.get('email', 'Неизвестно')
        text = request.POST.get('text', 'Неизвестно')
        Requests.objects.create(name=name, phone=phone, email=email, text=text)
        messages.success(request, 'Ваша заявка принята')

        request.session['message_exist'] = True
        return redirect('index')
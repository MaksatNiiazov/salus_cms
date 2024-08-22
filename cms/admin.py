from django.contrib import admin
from .models import MainBlock, AboutUs, Services, ServiceItem, Advantages, AdvantageItem, Developer, Building, Inquiry, \
    Contact, Phones, Social, WorkTime
from modeltranslation.admin import TranslationAdmin


class ServiceItemInline(admin.StackedInline):
    model = ServiceItem
    extra = 1  # Количество форм по умолчанию


class AdvantageItemInline(admin.StackedInline):
    model = AdvantageItem
    extra = 1  # Количество форм по умолчанию


@admin.register(MainBlock)
class MainBlockAdmin(TranslationAdmin):
    pass


@admin.register(AboutUs)
class AboutUsAdmin(TranslationAdmin):
    pass


@admin.register(Services)
class ServicesAdmin(TranslationAdmin):
    inlines = [ServiceItemInline]


@admin.register(ServiceItem)
class ServiceItemAdmin(TranslationAdmin):
    pass


@admin.register(Advantages)
class AdvantagesAdmin(TranslationAdmin):
    inlines = [AdvantageItemInline]


# @admin.register(AdvantageItem)
# class AdvantageItemAdmin(TranslationAdmin):
#     pass


@admin.register(Developer)
class DeveloperAdmin(TranslationAdmin):
    pass


@admin.register(Building)
class BuildingAdmin(TranslationAdmin):
    pass


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')  # Отображаемые поля в списке


class PhonesInline(admin.StackedInline):
    model = Phones
    extra = 0


class SocialInline(admin.StackedInline):
    model = Social
    extra = 0


class WorkTimeInline(admin.StackedInline):
    model = WorkTime
    extra = 0


@admin.register(Contact)
class ContactAdmin(TranslationAdmin):
    inlines = [PhonesInline, SocialInline, WorkTimeInline]


from modeltranslation.translator import register, TranslationOptions
from .models import MainBlock, AboutUs, Services, ServiceItem, Advantages, AdvantageItem, Developer, Building, Inquiry, \
    Contact


@register(MainBlock)
class MainBlockTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'first_text_title', 'first_text', 'second_text_title', 'second_text')


@register(AboutUs)
class AboutUsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Services)
class ServicesTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(ServiceItem)
class ServiceItemTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Advantages)
class AdvantagesTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(AdvantageItem)
class AdvantageItemTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Developer)
class DeveloperTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Building)
class BuildingTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Inquiry)
class InquiryTranslationOptions(TranslationOptions):
    fields = ('name', 'message')


@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields = ('text', 'small_text', 'phone_text')

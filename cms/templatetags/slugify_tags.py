from django import template
from django.utils.text import slugify

register = template.Library()


@register.filter(name='slugify_name')
def slugify_name(name):
    return slugify(name)

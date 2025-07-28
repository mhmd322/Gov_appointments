from django import template

register = template.Library()

@register.filter
def split_arabic(value, sep="،"):
    return value.split(sep)
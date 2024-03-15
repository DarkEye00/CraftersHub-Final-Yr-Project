# custom_filters.py
from django import template

register = template.Library()


@register.filter(name="multiply")
def multiply(value, arg):
    value = float(value)
    arg = float(arg)
    subtotal = value * arg
    return subtotal

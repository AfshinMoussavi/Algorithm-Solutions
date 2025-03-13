
from django import template

register = template.Library()

@register.filter
def convert_numbers_to_persian(text):
    persian_numbers = {'0': '۰', '1': '۱', '2': '۲', '3': '۳', '4': '۴', '5': '۵', '6': '۶', '7': '۷', '8': '۸', '9': '۹'}
    persian_text = ''.join(persian_numbers.get(char, char) for char in text)
    return persian_text

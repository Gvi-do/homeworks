
from django import template
from django.utils.html import format_html

register = template.Library()


@register.filter()
def check_color(elem):
    color = 'white'
    text = '-'
    if elem != '':
        text = float(elem)
        if text < 0:
            color = 'green'
        elif 1 < text < 2:
            color = 'LightSalmon'
        elif 2 <= text <= 5:
            color = 'Red'
        elif text > 5:
            color = 'DarkRed'
    return format_html(
            '<td style="background:{};">{}</td>',
            color,
            text,
        )


from django import template

register = template.Library()

# Custom template filter to convert a rating out of 5 into a percentage for star display.
@register.filter
def rating_percent(value):
    return round((value / 5) * 100, 1)
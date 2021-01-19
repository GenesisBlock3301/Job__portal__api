from django import template

register = template.Library()


def capitalize(value):
    if value:
        return value.capitalize()

register.filter('capitalize',capitalize)


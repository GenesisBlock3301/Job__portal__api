from django import template

register = template.Library()


def capitalize(value):
    if value:
        return value.capitalize()


def split_resume(value):
    if value:
        return value.split("/")[-1]


register.filter('capitalize',capitalize)
register.filter('split_resume',split_resume)


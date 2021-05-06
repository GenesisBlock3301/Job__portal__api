from django import template

register = template.Library()


def email_split(string):
    return string.split('@')[0]

def length(value):
    """Returns a boolean of whether the value is greater than an argument."""
    try:
        return len(value)
    except (ValueError, TypeError):
        return ''


def capitalize(value):
    if value:
        return value.capitalize()


def split_resume(value):
    if value:
        return value.split("/")[-1]


register.filter('split_resume',split_resume)
register.filter('capitalize',capitalize)
register.filter('email_split', email_split)
register.filter('length', length)

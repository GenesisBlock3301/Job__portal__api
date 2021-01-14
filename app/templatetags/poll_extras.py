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


register.filter('email_split', email_split)
register.filter('length', length)

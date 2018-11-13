#custom template filters are here.
from django import template
register = template.Library()

@register.filter(name='ala')

def ala(value,arg):
    return value.replace(arg,'')


#register.filter('ala', ala)

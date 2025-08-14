from django import template

register = template.Library()


@register.simple_tag
def dt_reverse(path_name, kwargs, datos):
    from django.urls import reverse
    acumulador = {}

    if kwargs:
        for k, v in kwargs.items():
            if v in datos:
                acumulador[k] = datos[v]
        return reverse(path_name, kwargs=acumulador)
    else:
        return reverse(path_name)
    

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter(name='underscore_to_space')
def underscore_to_space(value):
    if isinstance(value, str):
        return value.replace('_', ' ')
    return value
        
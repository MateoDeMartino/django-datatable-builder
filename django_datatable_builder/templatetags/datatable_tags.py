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
        
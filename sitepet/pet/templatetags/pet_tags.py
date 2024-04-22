from django import template
import pet.views


register = template.Library()

@register.simple_tag()
def get_elements():
    return pet.views.elems_db


@register.inclusion_tag('pet/list_elements.html')
def see_elements(elem_selected=0):
    elems = pet.views.elems_db
    return {'elems': elems, 'elem_selected': elem_selected}



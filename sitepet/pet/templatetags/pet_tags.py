from django import template
from django.db.models import Count

import pet.views
from pet.models import Element, TagPost

register = template.Library()

@register.inclusion_tag('pet/list_elements.html')
def see_elements(elem_selected=0):
    elems = Element.objects.annotate(total=Count('posts')).filter(total__gt=0)
    return {'elems': elems, 'elem_selected': elem_selected}


@register.inclusion_tag('pet/list_tags.html')
def see_tags():
    tags = TagPost.objects.annotate(total=Count('tags')).filter(total__gt=0)
    return {'tags': tags}


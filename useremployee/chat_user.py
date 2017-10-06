from django import template

register=template.Library()

@register.simple_tag
def localize_time(context,string):
    string=str(string)
    timezone=context['timezone']
    return "oke"
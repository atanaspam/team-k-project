from django import template

register = template.Library()

@register.filter
def is_manager(value):
    return value.groups.filter(name='Manager').exists()

@register.filter
def is_coach(value):
    return value.groups.filter(name='Coach').exists()

@register.filter
def is_parent(value):
    return value.groups.filter(name='Parent').exists()
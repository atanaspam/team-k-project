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

@register.filter(name='addcss')
def addcss(field, css):
   return field.as_widget(attrs={"class":css})

@register.filter
def orderby(data, field):
    return data.order_by(field)

@register.filter
def is_anonymous(value):
    return value.is_anonymous()

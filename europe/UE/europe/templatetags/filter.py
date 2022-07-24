from django.template.defaulttags import register

@register.filter
def get_submenus(submenus, menu):
    return submenus[menu]

@register.filter
def replace_spaces(submenu):
    return submenu.replace(" ", "_").lower()

@register.filter
def lower(item):
    return item.name.lower()
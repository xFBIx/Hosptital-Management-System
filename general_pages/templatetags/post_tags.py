from django import template

register = template.Library()

@register.filter(name='has_group') 
def has_group(user, group_name):
    if user.groups.filter(name=group_name).exists():
        return True
    elif not user.groups.all() and group_name == 'nouser' :
        return True

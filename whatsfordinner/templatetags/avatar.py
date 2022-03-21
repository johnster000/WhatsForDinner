from django import template
from django.template.loader import render_to_string
from colorhash import ColorHash

register = template.Library()

@register.filter
def avatar(user):
    letter = user.first_name[0].upper() + user.last_name[0].upper() if user.first_name else '?'
    color_ix = ColorHash(user.id)
    context = {'color_ix': color_ix.hex, 'letter': letter}
    return render_to_string('avatar.html', context)

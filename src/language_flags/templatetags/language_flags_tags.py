# language_flags/templatetags/language_flags_tags.py
# -*- coding: utf-8 -*-

import random

from django import template
from django.conf import settings


register = template.Library()

language_flags = {
    'de': ('de', 'at', 'ch'),
    'en': ('gb', 'us', 'au', 'nz', 'ie', 'ca'),
}


@register.inclusion_tag('language_flags/flagrow.html', takes_context=True)
def flags_for_language(context, count, language):
    count = int(count)
    flags = language_flags.get(language, [language])
    if len(flags) > count:
        flags = [flags[0]] + random.sample(flags[1:], count-1)
    return {'STATIC_URL': settings.STATIC_URL, 'flags': flags}

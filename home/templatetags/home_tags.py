from django import template
from ..models import Fest

register = template.Library()

@register.simple_tag
def get_menus(booth):
    detail = booth.detail
    menus = detail.split(",")
    return menus

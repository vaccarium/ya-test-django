# -*- coding: utf-8 -*-
from django import template

register = template.Library()

@register.filter
def timedelta(value):
	days = value.days
	hours = value.seconds / (60*60)
	minutes = (value.seconds % (60*60)) / 60
	if days:
		return u"{} дн {} ч {} мин".format(days, hours, minutes)
	elif hours:
		return u"{} ч {} мин".format(hours, minutes)
	else:
		return u"{} мин".format(minutes)

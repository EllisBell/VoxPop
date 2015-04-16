from django import template
from voxpop.models import Firm

register = template.Library()

@register.inclusion_tag('voxpop/firms.html')
def get_firms():
	firms = Firm.objects.all().order_by('name')
	return {'firm_list': firms}
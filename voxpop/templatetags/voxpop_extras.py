from django import template
from voxpop.models import Firm

register = template.Library()

@register.inclusion_tag('voxpop/firms.html')
def get_firms():
	return {'firm_list': Firm.objects.all()}
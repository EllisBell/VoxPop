from django import template
from voxpop.models import Firm

from voxpop.views import get_split_list

register = template.Library()

@register.inclusion_tag('voxpop/firms.html')
def get_newfirms():
	firms = Firm.objects.all().order_by('name')
	firmlists = get_split_list(firms)
	return {'firmlists': firmlists}
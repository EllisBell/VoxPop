from django import template
from voxpop.models import Firm

from voxpop.views import get_split_list

register = template.Library()

@register.inclusion_tag('voxpop/firms.html')
def get_newfirms():
	#get all firms; note use of .extra(select...) to make all names lower case before ordering (otherwise capitals come first)
	firms = Firm.objects.all().extra(select={'lower_name':'lower(name)'}).order_by('lower_name')
	firmlists = get_split_list(firms)
	return {'firmlists': firmlists}
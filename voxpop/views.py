from django.shortcuts import render
from django.http import HttpResponse
from voxpop.models import Firm, Review

# Create your views here.

def index(request):
	context_dict = {}
	context_dict['test'] = "yo yo yo"
	firms = Firm.objects.all()
	print firms
	context_dict['firms'] = firms
	return render(request, 'voxpop/index.html', context_dict)

# used for search - returns list of firms based on query
def get_firm_list(starts_with=''):
	firm_list = []
	if starts_with:
		firm_list = Firm.objects.filter(name__istartswith=starts_with)

	return firm_list

# def suggest_firm(request):
# 	firm_list = []
# 	starts_with = ''
# 	if request.method == 'GET':
# 		starts_with = request.GET['suggestion']

# 	firm_list = get_firm_list(8, starts_with)

# 	return render(request, 'voxpop/firm_list.html', {'firm_list':firm_list})

# calls get firm list above
# returns html with the firms matching search query (or all firms if query empty)
def firms(request):
	print "got here"
	firm_list = []
	starts_with = ''
	if request.method == 'GET':
		query = request.GET['query']

	
	if(query==''):
		firm_list = Firm.objects.all()
	else:
		firm_list = get_firm_list(query)

	return render(request, 'voxpop/firms.html', {'firm_list':firm_list})


from django.shortcuts import render
from django.http import HttpResponse
from voxpop.models import Firm, Review

# Create your views here.

def index(request):
	#context_dict = {}
	#context_dict['test'] = "yo yo yo"
	#firms = Firm.objects.all().order_by('name')
	#print firms
	#context_dict['firms'] = firms
	return render(request, 'voxpop/index.html')

def newhome(request):
	context_dict = {}
	allfirms = Firm.objects.all()
	num = len(allfirms)
	
	# want to have rows of 3 firms in template
	# get number of rows here
	if num%3 == 0:
		rows = num/3
	else:
		rows = (num/3) + 1

	firmindex = 0 # index for list of all firms
	firmlists = [] # list to store sublists of firms

	for i in range(0, rows): #for each row...
		minilist = [] # sublist of firms
		for i in range(0, 3): # get 3 firms
			if(firmindex < num): # check firmindex still within range
				minilist.append(allfirms[firmindex]) # add firm to sublist
				firmindex+=1 # increment index in full list
		firmlists.append(minilist) # add this sublist to metalist

	# N.B. - consider sending just the full list and then having logic in template, like so?:
	# if counter-1%3==0 AND counter%2==0, open row, column, firm is even
	# else if counter%3==0 AND counter%2==0, close row, column, firm is even
	# else if counter-1%3==0, open row, colum, firm is odd
	# else if counter%3==0, close row, colum, firm is odd
	# else if counter%2==0, just column, firm is even
	# else, just column, firm is odd

	context_dict['firmlists'] = firmlists

	return render(request, 'voxpop/newhome.html', context_dict)

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
		firm_list = Firm.objects.all().order_by('name')
	else:
		firm_list = get_firm_list(query)

	return render(request, 'voxpop/firms.html', {'firm_list':firm_list})

def show_reviews(request):
	reviews = []
	firm_id = None
	if request.method == 'GET':
		firm_id = request.GET['firm_id']
		
	firm = Firm.objects.get(id=firm_id)

	reviews = Review.objects.filter(firm=firm)
	return render(request, 'voxpop/reviews.html', {'reviews': reviews})


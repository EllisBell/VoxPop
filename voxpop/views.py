from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from voxpop.models import Firm, Review
from voxpop.forms import ReviewForm
import datetime

# Create your views here.


def index(request):
	latest_revs = Review.objects.all().order_by('-dt')[:3]

	return render(request, 'voxpop/index.html', {'latest_reviews': latest_revs})


def firms(request):
	context_dict = {}
	query = ''
	if request.method == 'GET':
		query = request.GET['query']
	
	if query=='':
		firm_list = Firm.objects.all().order_by('name')
	else:
		firm_list = get_firm_list(query)

	#firmlists = get_split_list(firm_list)

	#context_dict['firmlists'] = firmlists
	if len(firm_list) > 3:
		context_dict['too_many'] = True

	context_dict['firm_list'] = firm_list


	print "got here"

	return render(request, 'voxpop/newFirms.html', context_dict)

# used for search - returns list of firms based on query
#TODO - improve this... e.g. when people try "e" try "&" as well
def get_firm_list(query=''):
	firm_list = []
	if query:
		firm_list = Firm.objects.filter(name__icontains=query).extra(select={'lower_name':'lower(name)'}).order_by('lower_name')

	return firm_list


# takes list and splits it up into list of lists, each containing 3 items
def get_split_list(firmlist):
	
	num = len(firmlist)
	
	firmindex = 0 # index for list of all firms
	firmlists = [] # list to store sublists of firms

	#check for empty list coming in; if list is empty, return empty list of lists
	if num==0:
		return firmlists

	# want to have rows of 3 firms in template
	# get number of rows here
	if num%3 == 0:
		rows = num/3
	else:
		rows = (num/3) + 1

	for i in range(0, rows): #for each row...
		minilist = [] # sublist of firms
		for i in range(0, 3): # get 3 firms
			if(firmindex < num): # check firmindex still within range
				minilist.append(firmlist[firmindex]) # add firm to sublist
				firmindex+=1 # increment index in full list
		firmlists.append(minilist) # add this sublist to metalist

	# N.B. - consider sending just the full list and then having logic in template, like so?:
	# if counter-1%3==0 AND counter%2==0, open row, column, firm is even
	# else if counter%3==0 AND counter%2==0, close row, column, firm is even
	# else if counter-1%3==0, open row, colum, firm is odd
	# else if counter%3==0, close row, colum, firm is odd
	# else if counter%2==0, just column, firm is even
	# else, just column, firm is odd

	return firmlists


def reviews(request, firm_id):
	context_dict = {}
	
	try:
		reviews = []
			
		firm = Firm.objects.get(id=firm_id)
		reviews = Review.objects.filter(firm=firm)

		context_dict['firm'] = firm
		context_dict['reviews'] = reviews

	# in case firm with the id does not exist
	except Firm.DoesNotExist:
		pass

	return render(request, 'voxpop/reviews.html', context_dict)


#testing - to be completed
##TODO - change layout/look of form
#TODO - find out how to redisplay form with error messages
def newreview(request, firm_id):
	context_dict = {}

	try:
		firm = Firm.objects.get(id=firm_id)
	except Firm.DoesNotExist:
		firm = None

	if request.method == 'POST':
		form = ReviewForm(request.POST)
		if form.is_valid():
			if firm:
				r = form.save(commit=False)
				r.firm = firm
				r.save()
				return HttpResponseRedirect('/voxpop/') #change this to redirect to thank you page

	form = ReviewForm()
	context_dict['firm'] = firm
	context_dict['form'] = form

	return render(request, 'voxpop/newreview.html', context_dict)


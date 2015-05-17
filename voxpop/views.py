from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.db.models import Q
from voxpop.models import Firm, Review
from voxpop.forms import ReviewForm
import datetime
import operator

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
	context_dict['query'] = query


	print "got here"

	return render(request, 'voxpop/newFirms.html', context_dict)

# used for search - returns list of firms based on query
#TODO - improve this... e.g. potentially when people try "e" try "&" as well?
# split query string into individual words then check if firm name has all of the words
# to avoid checking for exact phrases - e.g. "vieira almeida" will get a match, no need for the "de"
# a bit of black magic using reduce, operator and Q
def get_firm_list(query=''):
	firm_list = []
	if query:
		word_list = query.split()
		firm_list = Firm.objects.filter(reduce(operator.and_, (Q(name__contains=word) for word in word_list)))
		#this is the same (I think) as filter(name contains word) & filter(name contains word) & filter(name contains word)

	return firm_list

# ATTENTION as it stands this is a uselss relic
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
		context_dict['average'] = get_average(reviews)

	# in case firm with the id does not exist
	except Firm.DoesNotExist:
		pass

	return render(request, 'voxpop/reviews.html', context_dict)

def get_average(reviews):
	total = 0
	num_rev = len(reviews)

	if num_rev == 0:
		return "n/a"

	for review in reviews:
		total += review.rating

	average = float(total) / num_rev
	avg_two_dec_places = "%.2f" % average
	return avg_two_dec_places


# deals with new review page / form
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
				return HttpResponseRedirect('/voxpop/newreview/thanks') #change this to redirect to thank you page
	else:
		form = ReviewForm()
	
	context_dict['firm'] = firm
	context_dict['form'] = form

	return render(request, 'voxpop/newreview.html', context_dict)

# thank you page for new reviews
def thanks(request):
	return render(request, 'voxpop/thanks.html')


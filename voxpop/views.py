from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	context_dict = {}
	context_dict['test'] = "yo yo yo"
	return render(request, 'voxpop/index.html', context_dict)

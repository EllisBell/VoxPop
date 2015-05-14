from django.conf.urls import patterns, url
from voxpop import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	#url(r'^suggest_firm/$', views.suggest_firm, name='suggest_firm'),
	url(r'^firms/$', views.firms, name='firms'),
	url(r'^reviews/(?P<firm_id>[0-9]+)/$', views.reviews, name='reviews'),
	url(r'^newreview/$', views.newreview, name='newreview'),
	url(r'^newFirms/$', views.firms, name='firms'),
	)